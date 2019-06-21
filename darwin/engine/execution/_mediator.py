
import abc

class mediator(abc.ABC):

    def __init__(self, dmap, kwargs):

        # get the darwin param dict and the kwargs dict
        self._dmap = dmap
        self._kwargs = kwargs

    @abc.abstractmethod
    # def execute(self, m, n, engine, func, maps, max_itr):
    def execute(self, engine):
        pass


