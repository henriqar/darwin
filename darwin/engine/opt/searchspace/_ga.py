
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

        # call super to show basic data
        super.show()

        for i in range(self._m):

            print(f'Agent {i} -> ', end='')
            for j in range(self._n):
                fit = self._a[i].x[j]
                print(f'x[{j}]: {fit}   ', end='')
            print('fitness value: {}'.format(self._a[i].fit))

    def evaluate(self):
        pass

    def check(self):

        if not isinstance(self._pMutation, float):
            print(' -> Probability of mutation undefined')
            return 1
        else:
            return 0

