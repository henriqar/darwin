
from .searchspace import searchspace

class pso(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # PSO
        self._w = 0.0 # inertia weight
        self._w_min = 0.0 # lower bound for w - used for adaptive inertia weight
        self._w_max = 0.0 # upper bound for w - used for adaptive inertia weight
        self._c1 = 0.0 # c1 parameter
        self._c2 = 0.0 # c2 parameter

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass

