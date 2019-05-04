
from .searchspace import searchspace

class fpa(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # FPA
        self._beta = 0.0 # used to compute the step based on Levy Flight
        self._p = 0.0 # probability of local pollination


    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
