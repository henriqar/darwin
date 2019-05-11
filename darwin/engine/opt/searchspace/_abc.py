
from .searchspace import searchspace

class abc(searchspace):

    def __init__(self, trial_limit=None):

        # call super from searchspace base class
        super().__init__()

        if trial_limit == None:
            print('error: ABC requires taht trial limit be set')
            sys.exit(1)

        # ABC
        self._limit = 0.0 # number of trial limits for each food source

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

        if not isinstance(self._limit, float):
            print(' -> Number of trial limits must be greater than 0')
            return 1
        else:
            return 0
