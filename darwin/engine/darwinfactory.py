
import platform
import sys

from . import execution as dexec

from darwin.dsl.constants import constants as cnts

class darwinfactory():

    agent_factories = {}
    search_space_factories = {}

    @staticmethod
    def add_agent_factory(id, fact):
        darwinfactory.agent_factories[id] = fact

    @staticmethod
    def add_searchspace_factory(id, fact):
        darwinfactory.search_space_factories[id] = fact

    @staticmethod
    def create_agents(id):
        if id not in darwinfactory.agent_factories:
            darwinfactory.agent_factories[id] = \
                    eval('agt.' + id + '.factory()')
        return darwinfactory.agent_factories[id].create()

    @staticmethod
    def create_searchspace(id):
        if id not in darwinfactory.search_space_factories:
            darwinfactory.search_space_factories[id] = \
                    eval('agt.' + id + '.factory()')
        return darwinfactory.search_space_factories[id].create()

    @staticmethod
    def create_engine(engine=cnts.LOCAL, opt=''):

        if opt == '':
            print('error: optimization algorithm not specified')
            sys.exit(1)

        if engine == cnts.LOCAL:
            return dexec.local.local(opt)
        elif engine == cnts.HTCONDOR and platform.system == 'Linux':
            return dexec.clustering.clustering(opt)

