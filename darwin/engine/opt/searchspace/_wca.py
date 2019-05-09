
from .searchspace import searchspace

class wca(searchspace):

    def __init__(self, nsr=None, dmax=None):

        # call super from searchspace base class
        super().__init__()

        if nsr == None:
            print('error: WCA searchspace requires a "nsr" be set')
            sys.exit(1)

        if dmax == None:
            print('error: WCA searchspace requires a "dmax" be set')
            sys.exit(1)

        # WCA
        self._nsr = nsr # number of rivers
        self._dmax = dmax # raining process maximum distance

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass

