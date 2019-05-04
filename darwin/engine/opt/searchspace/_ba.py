
from .searchspace import searchspace

class ba(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # BA
        self._f_min = 0.0 # minimum frequency
        self._f_max = 0.0 # maximum frequency
        self._r = 0.0 # pulse rate
        self._A = 0.0 # loudness

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass


