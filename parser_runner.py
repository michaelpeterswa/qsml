import error as error
import token as token
import lexer as lexer
import parser as parser
import sys


def main(filename):
    try:
        file_stream = open(filename, "r")
        the_lexer = lexer.Lexer(file_stream)
        the_parser = parser.Parser(the_lexer)
        runner(the_parser)
        file_stream.close()
    except FileNotFoundError:
        sys.exit("invalid filename %s" % filename)
    except error.QSMLError as e:
        file_stream.close()
        sys.exit(e)


def runner(the_parser):
    the_parser.parse()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: %s file" % sys.argv[0])
    main(sys.argv[1])
