
from . import *

class agtfactory():

    agents_init = {}

    @staticmethod
    def init_factory():

        agtfactory.agents_init['ga'] = ga
        # agtfactory.agents_init['abo'] = abo
        # agtfactory.agents_init['ba'] = ba
        # agtfactory.agents_init['bha'] = bha
        # agtfactory.agents_init['bsa'] = bsa
        # agtfactory.agents_init['bso'] = bso
        # agtfactory.agents_init['cs'] = cs
        # agtfactory.agents_init['de'] = de
        # agtfactory.agents_init['fa'] = fa
        # agtfactory.agents_init['fpa'] = fpa
        # agtfactory.agents_init['gp'] = gp
        # agtfactory.agents_init['hs'] = hs
        # agtfactory.agents_init['jade'] = jade
        # agtfactory.agents_init['loa'] = loa
        # agtfactory.agents_init['mbo'] = mbo
        # agtfactory.agents_init['pso'] = pso
        # agtfactory.agents_init['sa'] = sa
        # agtfactory.agents_init['wca'] = wca

    @staticmethod
    def create_agent(id, n):
        return agtfactory.agents_init[id](n)
