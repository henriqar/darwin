
from .searchspace import searchspace

class wca(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # WCA
        self._nsr = 0.0 # number of rivers
        self._dmax = 0.0 # raining process maximum distance

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass

