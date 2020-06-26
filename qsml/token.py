# Q S M L
# Token Class
# michaelpeterswa 2020

# for the format
STAR = "STAR"  # *
DOLLAR = "DOLLAR"  # $
COLON = "COLON"  # :
EOS = "EOS"  # end of stream

# for the values
COMMENT = "COMMENT"
TEXT = "TEXT"
VALUE = "VALUE"

# for the future
SLASH = "SLASH"  # /

# not currently in use
L_BRACK = "L_BRACK"  # <
R_BRACK = "R_BRACK"  # >
DOT = "DOT"  # .


class Token(object):
    # init method
    def __init__(self, tokentype, lexeme, line):
        self.tokentype = tokentype
        self.lexeme = lexeme
        self.line = line

    def __str__(self):
        return self.tokentype + " :: " + str(self.lexeme)
