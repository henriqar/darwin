
from .searchspace import searchspace

class de(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # DE
        self._mutation_factor = 0.0 # Mutation factor
        self._cross_probability = 0.0


    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
