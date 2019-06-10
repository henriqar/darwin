
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class abc(searchspace):

    def __init__(self, m, n, trial_limit=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('abc', n))

        if trial_limit == None:
            print('error: ABC requires taht trial limit be set')
            sys.exit(1)

        # ABC
        self._limit = 0.0 # number of trial limits for each food source

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

        if not isinstance(self._limit, float):
            print(' -> Number of trial limits must be greater than 0')
            return 1
        else:
            return 0
