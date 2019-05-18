
from . import *

class clusterfactory():

    cluster_init = {}

    @staticmethod
    def init_factory():

        clusterfactory.cluster_init['ga'] = ga
        # clusterfactory.cluster_init['abo'] = abo
        # clusterfactory.cluster_init['ba'] = ba
        # clusterfactory.cluster_init['bha'] = bha
        # clusterfactory.cluster_init['bsa'] = bsa
        # clusterfactory.cluster_init['bso'] = bso
        # clusterfactory.cluster_init['cs'] = cs
        # clusterfactory.cluster_init['de'] = de
        # clusterfactory.cluster_init['fa'] = fa
        # clusterfactory.cluster_init['fpa'] = fpa
        # clusterfactory.cluster_init['gp'] = gp
        # clusterfactory.cluster_init['hs'] = hs
        # clusterfactory.cluster_init['jade'] = jade
        # clusterfactory.cluster_init['loa'] = loa
        # clusterfactory.cluster_init['mbo'] = mbo
        # clusterfactory.cluster_init['pso'] = pso
        # clusterfactory.cluster_init['sa'] = sa
        # clusterfactory.cluster_init['wca'] = wca

    @staticmethod
    def create_clustering_execution(id, kwarg_dict):
        return clusterfactory.cluster_init[id](**kwarg_dict)
