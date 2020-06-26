# Q S M L
# Lexer Class
# michaelpeterswa 2020

import token
import error


class Lexer(object):
    def __init__(self, input_stream):
        self.line = 1
        self.input_stream = input_stream
        self.symbols = ["*", "$", ":"]

    def __peek(self):
        pos = self.input_stream.tell()
        symbol = self.input_stream.read(1)
        self.input_stream.seek(pos)
        return symbol

    def __read(self):
        if self.__peek() == "\n":
            self.line += 1
        return self.input_stream.read(1)

    def __comment_start(self, val):
        if val == "<":
            return True
        else:
            return False

    def next_token(self):
        peekValue = self.__peek()

        if peekValue == "":
            return token.Token(token.EOS, "", self.line)

        elif peekValue.isdigit():
            curr_val = ""
            while self.__peek().isdigit():
                curr_val += self.__read()
            return token.Token(token.VALUE, curr_val, self.line)

        elif peekValue.isalpha():
            curr_val = self.__read()  # at least one letter
            while self.__peek().isalpha() or self.__peek() == ".":
                curr_val += self.__read()
            return token.Token(token.TEXT, curr_val, self.line)

        elif self.__comment_start(peekValue):
            comment = ""
            self.__read()  # eat preliminary <
            while self.__peek() != ">":
                comment += self.__read()
            self.__read()
            return token.Token(token.COMMENT, comment, self.line)

        elif peekValue in self.symbols:
            if peekValue == "*":
                self.__read()
                return token.Token(token.STAR, "*", self.line)
            elif peekValue == "$":
                self.__read()
                return token.Token(token.DOLLAR, "$", self.line)
            elif peekValue == ":":
                self.__read()
                return token.Token(token.COLON, ":", self.line)
            else:
                raise error.QSMLError(
                    "unknown error occured - symbol mismatch", self.line
                )

        elif peekValue.isspace():
            self.__read()
            return self.next_token()

        else:
            raise error.QSMLError("unknown error occurred (end)", self.line)
