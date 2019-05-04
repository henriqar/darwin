
from .searchspace import searchspace

class bsa(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # BSA
        self._mix_rate = 0.0 # controls the number of elements of individuals that will mutate in a trial
        self._F = 0.0 # controls the amplitude of the search-direction matrix (oldS - s)

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
