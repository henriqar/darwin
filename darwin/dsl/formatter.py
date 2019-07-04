
import abc

class Formatter(abc.ABC):

    @abc.abstractmethod
    def format(self, data):
        raise NotImplementedError
