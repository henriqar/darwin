
from .searchspace import searchspace

class mbo(searchspace):

    def __init__(self, k=None, X=None, M=None):

        # call super from searchspace base class
        super().__init__()

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
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
