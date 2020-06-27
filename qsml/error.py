# Q S M L
# Error Class
# michaelpeterswa 2020


class QSMLError(Exception):
    def __init__(self, message, line):
        self.message = message
        self.line = line

    def __str__(self):
        msg = self.message
        line = self.line
        return "%s at line %i" % (msg, line)
