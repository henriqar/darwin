
import abc
import sys

class job(abc.ABC):

    def __init__(self, func):

        # save the func where it is used
        self._func = func

    @abc.abstractmethod
    # def exec(self, func, args):
    def exec(self, args):
        return sys.maxsize
