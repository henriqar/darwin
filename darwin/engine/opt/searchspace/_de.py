
from .searchspace import searchspace

class de(searchspace):

    def __init__(self, mutation_factor=None, crossover_probability=None):

        # call super from searchspace base class
        super().__init__()

        if mutation_factor == None:
            print('error: DE requires that "mutation_factor" be set')
            sys.exit(1)

        if crossover_probability == None:
            print('error: DE requires that "crossover_probability" be set')
            sys.exit(1)

        # DE
        self._mutation_factor = 0.0 # Mutation factor
        self._cross_probability = 0.0

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
        pass
