# Q S M L
# Lexer Runner Program
# michaelpeterswa 2020

import sys
import qsml


def main(filename):
    try:
        infile = open(filename, "r")
        run(infile)
        infile.close()
    except FileNotFoundError:
        sys.exit("invalid filename %s" % filename)
    except qsml.error.QSMLError as e:
        infile.close()
        sys.exit(e)


def run(file_stream):
    lexer_obj = qsml.lexer.Lexer(file_stream)
    token_obj = lexer_obj.next_token()
    while token_obj.tokentype != qsml.token.EOS:
        print(token_obj)
        token_obj = lexer_obj.next_token()
    print(token_obj)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: %s file" % sys.argv[0])
    main(sys.argv[1])
