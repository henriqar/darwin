
from .searchspace import searchspace

class abc(searchspace):

    def __init__(self, trial_limit=None):

        # call super from searchspace base class
        super().__init__()

        if trial_limit == None:
            print('error: ABC requires taht trial limit be set')
            sys.exit(1)

        # ABC
        self._limit = 0.0 # number of trial limits for each food source

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
