# Q S M L
# Handler
# michaelpeterswa 2020

from .token import *
from .lexer import Lexer
from .error import QSMLError
from .parser import Parser
from .dumperror import QSMLDumpError
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
            if isinstance(group, str):
                data += "* %s *\n\n" % group
                if collection:
                    for sym, amt in collection.items():
                        if isinstance(sym, str) and isinstance(amt, int):
                            data += "\t$ %s : %s\n" % (sym, amt)
                        else:
                            raise QSMLDumpError(
                                "Either symbol or amount is incorrectly formed"
                            )
                    data += "\n"
            else:
                raise QSMLDumpError("Group Name not String")

        outfile.write(data)
