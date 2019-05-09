
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
        pass

    def evaluate(self):
        pass

    def check(self):
        pass

