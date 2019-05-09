
import sys

from .searchspace import searchspace

class ga(searchspace):

    def __init__(self, mutation_probability=None):

        # call super from searchspace base class
        super().__init__()

        if mutation_probability == None:
            print('error: GA searchspace requires a mutation probability value to work')
            sys.exit(1)

        # GA
        self._pReproduction = 0.0 # probability of reproduction
        self._pMutation = mutation_probability # probability of mutation
        self._pCrossover = 0.0 # probability of crossover

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass

