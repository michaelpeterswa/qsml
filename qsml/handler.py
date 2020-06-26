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
        with open(filename, "r") as file_stream:
            lexer_obj = Lexer(file_stream)
            parser_obj = Parser(lexer_obj)
            return parser_obj.parse()

    except FileNotFoundError:
        sys.exit("invalid filename %s" % filename)
    except QSMLError as e:
        raise e


def dump(self, filename):
    pass
