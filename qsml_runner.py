import qsml
import sys


def main(filename):
    try:
        file_stream = open(filename, "r")
        the_lexer = qsml.lexer.Lexer(file_stream)
        the_parser = qsml.parser.Parser(the_lexer)
        runner(the_parser)
        file_stream.close()
    except FileNotFoundError:
        sys.exit("invalid filename %s" % filename)
    except qsml.error.QSMLError as e:
        file_stream.close()
        sys.exit(e)


def runner(the_parser):
    the_parser.parse()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: %s file" % sys.argv[0])
    main(sys.argv[1])
