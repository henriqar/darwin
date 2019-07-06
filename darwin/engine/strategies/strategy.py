
import abc

class Strategy(abc.ABC):

    def __init__(self, max_iter, pspace):

        # get the darwin param dict and the kwargs dict
        self._max_itrs = max_iter
        self._pspace = pspace

    @abc.abstractmethod
    def execute_step(self):
       raise NotImplementedError


