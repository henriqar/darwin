
# from . import ga
from ._ga import ga

class strategyfactory():

    strategy_init = {}

    @staticmethod
    def init_factory():

        strategyfactory.strategy_init['ga'] = ga
        # strategyfactory.strategy_init['abo'] = abo
        # strategyfactory.strategy_init['ba'] = ba
        # strategyfactory.strategy_init['bha'] = bha
        # strategyfactory.strategy_init['bsa'] = bsa
        # strategyfactory.strategy_init['bso'] = bso
        # strategyfactory.strategy_init['cs'] = cs
        # strategyfactory.strategy_init['de'] = de
        # strategyfactory.strategy_init['fa'] = fa
        # strategyfactory.strategy_init['fpa'] = fpa
        # strategyfactory.strategy_init['gp'] = gp
        # strategyfactory.strategy_init['hs'] = hs
        # strategyfactory.strategy_init['jade'] = jade
        # strategyfactory.strategy_init['loa'] = loa
        # strategyfactory.strategy_init['mbo'] = mbo
        # strategyfactory.strategy_init['pso'] = pso
        # strategyfactory.strategy_init['sa'] = sa
        # strategyfactory.strategy_init['wca'] = wca

    @staticmethod
    def create_strategy(id, kwarg_dict):
        return strategyfactory.strategy_init[id](kwarg_dict)
