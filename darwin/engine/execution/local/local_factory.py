
# from . import ga
from ._ga import ga

class localfactory():

    local_init = {}

    @staticmethod
    def init_factory():

        localfactory.local_init['ga'] = ga
        # localfactory.local_init['abo'] = abo
        # localfactory.local_init['ba'] = ba
        # localfactory.local_init['bha'] = bha
        # localfactory.local_init['bsa'] = bsa
        # localfactory.local_init['bso'] = bso
        # localfactory.local_init['cs'] = cs
        # localfactory.local_init['de'] = de
        # localfactory.local_init['fa'] = fa
        # localfactory.local_init['fpa'] = fpa
        # localfactory.local_init['gp'] = gp
        # localfactory.local_init['hs'] = hs
        # localfactory.local_init['jade'] = jade
        # localfactory.local_init['loa'] = loa
        # localfactory.local_init['mbo'] = mbo
        # localfactory.local_init['pso'] = pso
        # localfactory.local_init['sa'] = sa
        # localfactory.local_init['wca'] = wca

    @staticmethod
    def create_local_execution(id, kwarg_dict):
        return localfactory.local_init[id](kwarg_dict)
