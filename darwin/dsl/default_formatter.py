
from . import Formatter

class DefaultFormatter(Formatter):

    def format(self, data):
        return str(data)
