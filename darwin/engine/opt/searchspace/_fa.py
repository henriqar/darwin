
from .searchspace import searchspace

class fa(searchspace):

    def __init__(self, alpha=None, beta=None, gamma=None):

        # call super from searchspace base class
        super().__init__()

        if alpha == None:
            print('error: FA requires that "alpha" be set')
            sys.exit(1)

        if beta == None:
            print('error: FA requires that "beta" be set')
            sys.exit(1)

        if gamma == None:
            print('error: FA requires that "gamma" be set')
            sys.exit(1)

        # FA
        self._alpha = 0  # randomized parameter
        self._beta_0 = 0 # attractiveness
        self._gamma = 0 # light absorption

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

        if not isinstance(self._alpha, float):
            print(' -> Randomized parameter undefined')
            return 1
        elif not isinstance(self._beta_0, float):
            print(' -> Attractiveness undefined')
            return 1
        elif not isinstance(self._gamma, float):
            print(' -> Light absorption undefined.')
            return 1
        else:
            return 0

