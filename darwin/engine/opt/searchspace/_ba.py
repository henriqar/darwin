
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class ba(searchspace):

    def __init__(self, m, n, f_min=None, f_max=None, A=None, r=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('ba', n))

        if f_min == None:
            print('error: BA requires that "f_min" be set')
            sys.exit(1)

        if f_max == None:
            print('error: BA requires that "f_max" be set')
            sys.exit(1)

        if A == None:
            print('error: BA requires that "A" be set')
            sys.exit(1)

        if r == None:
            print('error: BA requires that "r" be set')
            sys.exit(1)

        # BA
        self._f_min = float('nan') # minimum frequency
        self._f_max = float('nan') # maximum frequency
        self._r = float('nan') # pulse rate
        self._A = float('nan') # loudness

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

    def check():

        if not isinstance(self._f_min, float):
            print(' -> Minimum frequency undefined')
            return 1
        elif not isinstance(self._f_max, float):
            print(' -> Maximum frequency undefined')
            return 1
        elif not isinstance(self._r, float):
            print(' -> Pulse rate undefined')
            return 1
        elif not isinstance(self._A, float):
            print(' -> Loudness undefined')
            return 1
        else:
            return 0


