
from .searchspace import searchspace

class bsa(searchspace):

    def __init__(self, mix_rate=None, F=None):

        # call super from searchspace base class
        super().__init__()

        if mix_rate == None:
            print('error: BSA requires that "mix_rate" be set')
            sys.exit(1)

        if F == None:
            print('error: BSA requires that "F" be set')
            sys.exit(1)

        # BSA
        self._mix_rate = 0.0 # controls the number of elements of individuals that will mutate in a trial
        self._F = 0.0 # controls the amplitude of the search-direction matrix (oldS - s)

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
