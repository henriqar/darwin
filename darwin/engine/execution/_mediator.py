
import abc

class mediator(abc.ABC):

    def __init__(self, opt):

        # geet the opt algorithm used
        self._opt = opt

        # init vars
        self._nro_agents = 0

    def set_nro_agents(self, nro_agents):

        # save number of agents used
        self._nro_agents = nro_agents

    @abc.abstractmethod
    def execute(self):
        pass


