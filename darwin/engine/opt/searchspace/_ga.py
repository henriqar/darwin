
from .searchspace import searchspace

class ga(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # GA
        self._pReproduction = 0.0 # probability of reproduction
        self._pMutation = 0.0 # probability of mutation
        self._pCrossover = 0.0 # probability of crossover

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass

