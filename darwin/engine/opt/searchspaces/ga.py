
import copy
import logging
import sys

from darwin._constants import opt
from . import Searchspace

logger = logging.getLogger(__name__)

class Ga(Searchspace):

    def __init__(self, data):

        # call super from searchspace base class
        super().__init__(opt.GA)

        required = ('mutation_probability',)
        data.hasrequired(required)

        # GA
        self._pReproduction = 0.0 # probability of reproduction
        self._pMutation = data.mutation_probability # probability of mutation
        self._pCrossover = 0.0 # probability of crossover

    @property
    def pMutation(self):
        return self._pMutation

    def show(self):

        # call super to show basic data
        super().show()

        for i in range(self._m):

            print('Agent {} -> '.format(i), end='')
            for j in range(self._n):
                fit = self._a[i].x[j]
                print('x[{}]: {}   '.format(j, fit), end='')
            print('fitness value: {}'.format(self._a[i].fit))

    def update(self):

        for i in range(self.m):

            if self.a[i].fit < self._gfit:

                self._gfit = self.a[i].fit

                # for j in range(self._n):
                self._g = copy.deepcopy(self.a[i].x)


    def check(self):

        if not isinstance(self._pMutation, float):
            print(' -> Probability of mutation undefined')
            return 1
        else:
            return 0

