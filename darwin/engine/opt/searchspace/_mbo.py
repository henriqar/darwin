
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class mbo(searchspace):

    def __init__(self, m, n, k=None, X=None, M=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('mbo', n))

        if k == None:
            print('error: MBO searchspace requires a "k" be set')
            sys.exit(1)

        if X == None:
            print('error: MBO searchspace requires a "X" be set')
            sys.exit(1)

        if M == None:
            print('error: MBO searchspace requires a "M" be set')
            sys.exit(1)

        # MBO
        self._X = X # number of neighbour solutions to be shared with the next solution
        self._M = M # number of tours, i.e., the number of iterations for the leader
        self._leftSide = 0.0 # flag to know which bird will be changed
        self._k = k # number of neighbours solutions to be considered for MBO or number of clusters for BSO

    def show(self):

        # call super to show basic data
        super.show()

        for i in range(self._m):

            print(f'Agent {i} -> ', end='')
            for j in range(self._n):
                fit = self._a[i].x[j]
                print(f'x[{j}]: {fit}   ', end='')

            print('fitness value: {}'.format(self._a[i].fit))

    def evaluate(self, func, args):

        for i in range(s.m):

            fitness = s.a[i].evaluate(args)
            s.a[i].fit = fitness

    def check(self):

        if not isinstance(self._k, float):
            print(' -> Number of neighbours solutions to be considered undefined')
            return 1
        elif not isinstance(self._X, float):
            print(' -> Number of neighbour solutions to be shared with the next solution undefined')
            return 1
        elif not isinstance(self._M, float):
            print(' -> Number of tours undefined')
            return 1
        elif self._X >= self._k:
            print(' -> Number of neighbour shared should be smaller than the number of neighbours considered')
            return 1
        elif self._m < 3:
            print(' -> Number of birds should be bigger than or equal to 3')
            return 1
        else:
            return 0
