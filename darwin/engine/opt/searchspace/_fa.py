
from .searchspace import searchspace

class fa(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

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

