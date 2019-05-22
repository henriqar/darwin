
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class bso(searchspace):

    def __init__(self, m, n, k=None, p_one_cluster=None, p_one_center=None, p_two_center=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('bso', n))

        if k == None:
            print('error: BSO requires that "k" be set')
            sys.exit(1)

        if p_one_cluster == None:
            print('error: BSO requires that "p_one_cluster" be set')
            sys.exit(1)

        if p_one_center == None:
            print('error: BSO requires that "p_one_center" be set')
            sys.exit(1)

        if p_two_center == None:
            print('error: BSO requires that "p_two_center" be set')
            sys.exit(1)

        # prob of selecting a cluster center
        self._p_one_cluster = float('nan')

        # prob of randomly selecting an idea from a probabilistic selected
        # cluster
        self._p_one_center = float('nan')

        # prob of of creating a random comb of two probabilistic selected
        # clusters
        self._p_two_centers = float('nan')

        # number of neighbours solutions to be considered for MBO or number of
        #clusters for BSO
        self._k = float('nan')

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

        if not isinstance(self._k, float) or self._k < 1:
            print(' -> Number of clusters undefined or invalid')
            return 1
        elif not isinstance(self._p_one_cluster, float):
            print(' -> Probability of selecting a cluster center undefined')
            return 1
        elif not isinstance(self._p_one_center, float):
            print(' -> Probability of randomly selecting an idea from a probabilistic selected cluster undefined')
            return 1
        elif not isinstance(self._p_two_centers, float):
            print(' -> Probability of of creating a random combination of two probabilistic selected clusters undefined')
            return 1
        else:
            return 0
