
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
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
