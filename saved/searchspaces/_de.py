
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class de(searchspace):

    def __init__(self, m, n, mutation_factor=None, crossover_probability=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('de', n))

        if mutation_factor == None:
            print('error: DE requires that "mutation_factor" be set')
            sys.exit(1)

        if crossover_probability == None:
            print('error: DE requires that "crossover_probability" be set')
            sys.exit(1)

        self._mutation_factor = float('nan')
        self._cross_probability = float('nan')

    def show(self):

        # call super to show basic data
        super.show()

        for i in range(self._m):

            print('Agent {} -> '.format(i), end='')
            for j in range(self._n):
                fit = self._a[i].x[j]
                print('x[{}]: {}   '.format(j, fit), end='')
            print('fitness value: {}'.format(self._a[i].fit))

    def evaluate(self):
        pass

    def check(self):
        pass
