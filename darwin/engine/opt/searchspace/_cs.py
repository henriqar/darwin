
from .searchspace import searchspace

class cs(searchspace):

    def __init__(self, alpha=None, p=None, beta=None):

        # call super from searchspace base class
        super().__init__()

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
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
