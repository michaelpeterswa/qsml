# Q S M L
# Runner Program
# michaelpeterswa 2020


import token
import lexer
import error
import sys


def main(filename):
    try:
        infile = open(filename, "r")
        run(infile)
        infile.close()
    except FileNotFoundError:
        sys.exit("invalid filename %s" % filename)
    except error.QSMLError as e:
        infile.close()
        sys.exit(e)


def run(file_stream):
    lexer_obj = lexer.Lexer(file_stream)
    token_obj = lexer_obj.next_token()
    while token_obj.tokentype != token.EOS:
        print(token_obj)
        token_obj = lexer_obj.next_token()
    print(token_obj)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: %s file" % sys.argv[0])
    main(sys.argv[1])
