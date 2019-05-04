
from .searchspace import searchspace

class abc(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # ABC
        self._limit = 0.0 # number of trial limits for each food source

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
