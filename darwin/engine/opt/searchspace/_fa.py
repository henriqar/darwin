
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class fa(searchspace):

    def __init__(self, m, n, alpha=None, beta=None, gamma=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('fa'))

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
        self._alpha = float('nan')  # randomized parameter
        self._beta_0 = float('nan') # attractiveness
        self._gamma = float('nan') # light absorption

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

