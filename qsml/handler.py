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


def dump(filename, dict_obj, title="QSML File v1.0"):

    with open(filename, "w+") as outfile:
        data = "< %s >\n\n" % title
        for group, collection in dict_obj.items():
            data += "* %s *\n\n" % group
            if collection:
                for sym, amt in collection.items():
                    data += "\t$ %s : %s\n" % (sym, amt)
                data += "\n"
        outfile.write(data)
