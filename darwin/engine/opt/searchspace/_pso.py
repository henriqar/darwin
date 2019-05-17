
import sys

from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class pso(searchspace):

    def __init__(self, m, n, c1=None, c2=None, w=None, w_min=None, w_max=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('pso'))

        if c1 == None:
            print('error: PSO searchspace requires a "c1" be set')
            sys.exit(1)

        if c2 == None:
            print('error: PSO searchspace requires a "c2" be set')
            sys.exit(1)

        if w == None:
            print('error: PSO searchspace requires a "w" be set')
            sys.exit(1)

        if w_min == None:
            print('error: PSO searchspace requires a "w_min" be set')
            sys.exit(1)

        if w_max == None:
            print('error: PSO searchspace requires a "w_max" be set')
            sys.exit(1)

        # PSO
        self._w = w # inertia weight
        self._w_min = w_min # lower bound for w - used for adaptive inertia weight
        self._w_max = w_max # upper bound for w - used for adaptive inertia weight
        self._c1 = c1 # c1 parameter
        self._c2 = c2 # c2 parameter

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

        if not isinstance(self._w, float):
            print(' -> Inertia weight undefined')
            return 1
        elif not isinstance(self._w_min, float):
            print(' -> Minimum inertia weight undefined')
            return 1
        elif not isinstance(self._w_max, float):
            print(' -> Maximum inertia weight undefined')
            return 1
        elif not isinstance(self._c1, float):
            print(' -> C1 parameter undefined')
            return 1
        elif not isinstance(self._c2, float):
            print(' -> C2 parameter undefined')
            return 1
        else:
            return 0



