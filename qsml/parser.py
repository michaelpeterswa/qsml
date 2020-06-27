# Q S M L
# Parser Class
# michaelpeterswa 2020

from .token import *
from .lexer import Lexer
from .error import QSMLError
from .builder import Builder


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
        self.builder = Builder()
        self.current_group = None

    def parse(self):
        self.__advance()
        self.__enter()
        self.__eat(EOS, "expected EOS")
        return self.builder.get_data()

    def __advance(self):
        self.current_token = self.lexer.next_token()

    def __eat(self, tokentype, error_msg):
        if self.current_token.tokentype == tokentype:
            self.__advance()
        else:
            self.__error(error_msg)

    def __error(self, error_msg):
        s = error_msg + ', found "' + self.current_token.lexeme + '" in parser'
        l = self.current_token.line
        raise QSMLError(s, l)

    def __enter(self):
        if self.current_token.tokentype != EOS:
            self.__pathways()
            self.__enter()

    def __pathways(self):
        if self.current_token.tokentype == COMMENT:
            self.__comment()
        elif self.current_token.tokentype == STAR:
            self.__group()
        elif self.current_token.tokentype == DOLLAR:
            self.__kvp()
        else:
            raise QSMLError("unknown error occurred in parser", self.current_token.line)

    def __comment(self):
        self.__eat(COMMENT, "expected COMMENT")

    def __group(self):
        self.__eat(STAR, "expected *")
        self.builder.set_group(self.current_token.lexeme)
        self.current_group = self.current_token.lexeme
        self.__eat(TEXT, "expected TEXT")
        self.__eat(STAR, "expected *")

    def __kvp(self):
        grp = self.current_group
        self.__eat(DOLLAR, "expected $")

        stock = self.current_token.lexeme
        self.__eat(TEXT, "expected TEXT")
        self.__eat(COLON, "expected COLON")

        shares = self.current_token.lexeme
        self.__eat(VALUE, "expected VALUE")

        self.builder.add_to_group(grp, stock, int(shares))
