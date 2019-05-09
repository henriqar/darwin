
from .searchspace import searchspace

class pso(searchspace):

    def __init__(self, c1=None, c2=None, w=None, w_min=None, w_max=None):

        # call super from searchspace base class
        super().__init__()

        if c1 == None:
            print('error: PSO searchspace requires a "c1" be set')
            sys.exit(1)

        if c2 == None:
            print('error: PSO searchspace requires a "c2" be set')
            sys.exit(1)

        if w == None:
            print('error: PSO searchspace requires a "w" be set')
            sys.exit(1)

        if w_min == None:
            print('error: PSO searchspace requires a "w_min" be set')
            sys.exit(1)

        if w_max == None:
            print('error: PSO searchspace requires a "w_max" be set')
            sys.exit(1)

        # PSO
        self._w = w # inertia weight
        self._w_min = w_min # lower bound for w - used for adaptive inertia weight
        self._w_max = w_max # upper bound for w - used for adaptive inertia weight
        self._c1 = c1 # c1 parameter
        self._c2 = c2 # c2 parameter

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass

