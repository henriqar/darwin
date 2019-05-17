
import abc

class mediator(abc.ABC):

    def __init__(self, opt, kwargs):

        # geet the opt algorithm used
        self._opt = opt

        # init vars
        self._nro_agents = 0

        # max iterations
        self._max_itrs = 0

        # get the kwargs dict
        self._kwargs = kwargs

        # create variables
        self._nro_decision_vars = 0

    def set_nro_agents(self, nro_agents):

        # save number of agents used
        self._nro_agents = nro_agents

    def set_min_function(self, func):

        # sae the function to be minimized
        self._func = func

    def set_mappings(self, names, sets):

        # save parameters input by the user
        self._names = names
        self._sets = sets

    def set_max_iter(self, nro):

        # get max iterations
        self._max_itrs = nro

    def set_nro_decision_vars(self, val):

        # set decision variables
        self._nro_decision_vars = val

    @abc.abstractmethod
    def execute(self):
        pass


