
import sys

# from darwin.engine.execution._mediator import mediator
from darwin.engine.execution.local import local

from darwin.engine.opt import agtfactory as agf
from darwin.engine.opt import spfactory as spf

class fa(local):

    def execute(self, m, n, func, names, sets, max_itr):

        # create both factories for agents and searchspace
        agf.init_factory()
        spf.init_factory()

        # get the searchspace used
        opt_searchspace = spf.create_searchspace('fa', m, n, self._kwargs)

        # d = {}
        # # import pdb; pdb.set_trace()
        # for k, v in self._names.items():
        #     d[k] = self._sets[v][0]

        # self._func(*d)

