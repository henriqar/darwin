
from .searchspace import searchspace

class fpa(searchspace):

    def __init__(self, beta=None, p=None):

        # call super from searchspace base class
        super().__init__()

        if beta == None:
            print('error: FPA requires that "beta" be set')
            sys.exit(1)

        if p == None:
            print('error: FPA requires that "p" be set')
            sys.exit(1)

        # FPA
        self._beta = 0.0 # used to compute the step based on Levy Flight
        self._p = 0.0 # probability of local pollination


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

        if not isinstance(self._beta, float):
            print(' -> Beta parameter used to compute the step based on Levy Flight undefined')
            return 1
        elif not isinstance(self.__p, float):
            print(' -> Probability of local pollination undefined')
            return 1
        else:
            return 0
