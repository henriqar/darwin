
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class wca(searchspace):

    def __init__(self, m, n, nsr=None, dmax=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('wca', n))

        if nsr == None:
            print('error: WCA searchspace requires a "nsr" be set')
            sys.exit(1)

        if dmax == None:
            print('error: WCA searchspace requires a "dmax" be set')
            sys.exit(1)

        # WCA
        self._nsr = nsr # number of rivers
        self._dmax = dmax # raining process maximum distance

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

        if not isinstance(self._nsr, float):
            print(' -> Number of rivers undefined')
            return 1
        elif not isinstance(self._dmax, float):
            print(' -> Raining process maximum distance undefined')
            return 1
        else:
            return 0

