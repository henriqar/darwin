
from .searchspace import searchspace

class bha(searchspace):

    def __init__(self, f_min=None, f_max=None, A=None, r=None):

        # call super from searchspace base class
        super().__init__()

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
        pass


