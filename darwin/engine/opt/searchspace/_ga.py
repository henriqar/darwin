
import logging
import sys

from .searchspace import searchspace

__log = logging.getLogger('darwin')

class ga(searchspace):

    def __init__(self, engine, mutation_probability=None):

        # call super from searchspace base class
        super().__init__('ga', engine)

        if mutation_probability == None:
            __log.error('error: GA searchspace requires a mutation\
                    probability value to work')
            sys.exit(1)

        # GA
        self._pReproduction = 0.0 # probability of reproduction
        self._pMutation = mutation_probability # probability of mutation
        self._pCrossover = 0.0 # probability of crossover

    def show(self):

        # call super to show basic data
        super().show()

        for i in range(self._m):

            print('Agent {} -> '.format(i), end='')
            for j in range(self._n):
                fit = self._a[i].x[j]
                print('x[{}]: {}   '.format(j, fit), end='')
            print('fitness value: {}'.format(self._a[i].fit))

    def schedule(self):

        # send evaluations to execution engine
        for i in range(self.m):
            self.a[i].schedule()

    def update(self):

        for i in range(self.m):

            # get the intermediate value of the simulation
            fitness = self.a[i].intermediate

            if fitness < self.a[i].fit:
                self.a[i].fit = fitness

            if self.a[i].fit < self._gfit:

                self.gfit = self.a[i].fit

                for j in range(self._n):
                    self._g[j] = self.a[i].x[j]


    def check(self):

        if not isinstance(self._pMutation, float):
            print(' -> Probability of mutation undefined')
            return 1
        else:
            return 0

