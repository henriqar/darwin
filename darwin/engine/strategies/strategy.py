
import abc

class Strategy(abc.ABC):

    def __init__(self, data, pspace):

        # get the darwin param dict and the kwargs dict
        self._data = data
        self._pspace = pspace

    @abc.abstractmethod
    def execute_step(self):
       raise NotImplementedError


