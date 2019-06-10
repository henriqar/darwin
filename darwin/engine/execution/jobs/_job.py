
import abc
import sys

class job(abc.ABC):

    @abc.abstractmethod
    def exec(self, func, args):
        return sys.maxsize
