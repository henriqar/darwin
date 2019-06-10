
# from . import ga
from ._ga import ga

class enginefactory():

    engine_init = {}

    @staticmethod
    def init_factory():

        enginefactory.engine_init['ga'] = ga
        # enginefactory.engine_init['abo'] = abo
        # enginefactory.engine_init['ba'] = ba
        # enginefactory.engine_init['bha'] = bha
        # enginefactory.engine_init['bsa'] = bsa
        # enginefactory.engine_init['bso'] = bso
        # enginefactory.engine_init['cs'] = cs
        # enginefactory.engine_init['de'] = de
        # enginefactory.engine_init['fa'] = fa
        # enginefactory.engine_init['fpa'] = fpa
        # enginefactory.engine_init['gp'] = gp
        # enginefactory.engine_init['hs'] = hs
        # enginefactory.engine_init['jade'] = jade
        # enginefactory.engine_init['loa'] = loa
        # enginefactory.engine_init['mbo'] = mbo
        # enginefactory.engine_init['pso'] = pso
        # enginefactory.engine_init['sa'] = sa
        # enginefactory.engine_init['wca'] = wca

    @staticmethod
    def create_engine(id, kwarg_dict):
        return enginefactory.engine_init[id](kwarg_dict)
