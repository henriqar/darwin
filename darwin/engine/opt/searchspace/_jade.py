
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class jade(searchspace):

    def __init__(self, m, n, c=None, p=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('jade', n))

        # JADE
        self._c = c # rate of parameter adaptation
        self._p_greediness = p # determines the greediness of the mutation strategy

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

        if not isinstance(self._c, float):
            print(' -> c undefined')
            return 1
        elif not isinstance(self._p_greediness, float):
            print(' -> p undefined')
            return 1
        else:
            return 0
