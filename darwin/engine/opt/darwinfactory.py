
class darwinfactory():

    agent_factories = {}
    search_space_factories = {}

    @staticmethod
    def add_agent_factory(self, id, fact):
        darwinfactory.agent_factories[id] = fact

    @staticmethod
    def add_searchspace_factory(self, id, fact):
        darwinfactory.search_space_factories[id] = fact

    @staticmethod
    def create_agents(self, id):
        if not darwinfactory.agent_factories.has_key(id):
            darwinfactory.agent_factories[id] = \
                    eval(id + '.factory()')
        return darwinfactory.agent_factories[id].create()

    @staticmethod
    def create_searchspace(self, id):
        if not darwinfactory.search_space_factories.has_key(id):
            darwinfactory.search_space_factories[id] = \
                    eval(id + '.factory()')
        return darwinfactory.search_space_factories[id].create()

