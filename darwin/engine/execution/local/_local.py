
from darwin.engine.execution._mediator import mediator

from darwin.engine.opt import agtfactory as agtfct
from darwin.engine.opt import spfactory as spfct

class local(mediator):

    def execute(self):

        # create both factories for agents and searchspace
        agtfct.init_factory()
        spfct.init_factory()

        # get the searchspace used
        opt_searchspace = spfct.create_searchspace(self._opt)

        # get the number of agent used
        agents = []
        for i in range(self._nro_agents):
            agents.append(agtfct.create_agent(self._opt))

