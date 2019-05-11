
from .searchspace import searchspace

class abo(searchspace):

    def __init__(self, ratio_e=None, step_e=None):

        # call super from searchspace base class
        super().__init__()

        if ratio_e == None:
            print('error: ABC requires that ratio_e be set')
            sys.exit(1)

        if step_e == None:
            print('error: ABC requires that step_e be set')
            sys.exit(1)

        # ABO
        self._ratio_e = 0.0 #
        self._step_e = 0.0 #

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

        if not isinstance(self._ratio_e, float):
            print(' -> proportion of sunspot butterflies undefined.')
            return 1
        elif not isinstance(self._step_e, float):
            print(' -> step parameter undefined.')
            return 1
        else:
            return 0

