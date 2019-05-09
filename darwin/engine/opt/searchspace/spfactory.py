
from . import *

class spfactory():

    searchspace_init = {}

    @staticmethod
    def init_factory():

        spfactory.searchspace_init['ga'] = ga
        spfactory.searchspace_init['abo'] = abo
        spfactory.searchspace_init['ba'] = ba
        spfactory.searchspace_init['bha'] = bha
        spfactory.searchspace_init['bsa'] = bsa
        spfactory.searchspace_init['bso'] = bso
        spfactory.searchspace_init['cs'] = cs
        spfactory.searchspace_init['de'] = de
        spfactory.searchspace_init['fa'] = fa
        spfactory.searchspace_init['fpa'] = fpa
        spfactory.searchspace_init['gp'] = gp
        spfactory.searchspace_init['hs'] = hs
        spfactory.searchspace_init['jade'] = jade
        spfactory.searchspace_init['loa'] = loa
        spfactory.searchspace_init['mbo'] = mbo
        spfactory.searchspace_init['pso'] = pso
        spfactory.searchspace_init['sa'] = sa
        spfactory.searchspace_init['wca'] = wca

    @staticmethod
    def create_searchspace(id, kwarg_dict):
        return spfactory.searchspace_init[id](**kwarg_dict)
