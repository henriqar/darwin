
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class bsa(searchspace):

    def __init__(self, m, n, mix_rate=None, F=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('bsa'))

        if mix_rate == None:
            print('error: BSA requires that "mix_rate" be set')
            sys.exit(1)

        if F == None:
            print('error: BSA requires that "F" be set')
            sys.exit(1)

        # BSA

        # controls the number of elements of individuals that will mutate in a trial
        self._mix_rate = float('nan')

        # controls the amplitude of the search-direction matrix (oldS - s)
        self._F = 0.0

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):

        if not isinstance(self._mix_rate, float):
            print(' -> Mix Rate undefined')
            return 1
        elif self._F < 0:
            print(' -> F undefined')
            return 1
        else:
            return 0
