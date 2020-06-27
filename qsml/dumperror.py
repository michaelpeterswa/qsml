# Q S M L
# Dump Error Class
# michaelpeterswa 2020


class QSMLDumpError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        msg = self.message
        return "%s in dict" % (str(msg))
