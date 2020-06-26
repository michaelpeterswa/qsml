# Q S M L
# Handler
# michaelpeterswa 2020

from .token import *
from .lexer import Lexer
from .error import QSMLError
from .parser import Parser
import sys


def load(filename=None):
    try:
        file_stream = open(filename, "r")
        lexer_obj = Lexer(file_stream)
        parser_obj = Parser(lexer_obj)

        print(parser_obj.parse())

        file_stream.close()
    except FileNotFoundError:
        sys.exit("invalid filename %s" % filename)
    except QSMLError as e:
        file_stream.close()
        sys.exit(e)


def dump(self, filename):
    pass
