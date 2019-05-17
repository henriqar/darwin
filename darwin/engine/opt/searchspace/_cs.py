
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class cs(searchspace):

    def __init__(self, m, n, alpha=None, p=None, beta=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('cs'))

        if alpha == None:
            print('error: CS requires that "alpha" be set')
            sys.exit(1)

        if p == None:
            print('error: CS requires that "p" be set')
            sys.exit(1)

        if beta == None:
            print('error: CS requires that "beta" be set')
            sys.exit(1)

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
            print(' -> Step size undefined')
            return 1
        elif not isinstance(self._beta, float):
            print(' -> Beta parameter used to compute the step based on Levy Flight undefined')
            return 1
        elif not isinstance(self._p, float):
            print(' -> Switch probability undefined')
            return 1
        else:
            return 0
