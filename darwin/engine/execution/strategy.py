
import abc

class strategy(abc.ABC):

    def __init__(self, kwargs):

        # get the darwin param dict and the kwargs dict
        self._kwargs = kwargs

    @abc.abstractmethod
    # def execute(self, m, n, engine, func, maps, max_itr):
    def execute_step(self, engine):
       raise NotImplementedError


