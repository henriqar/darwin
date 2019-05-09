
from .searchspace import searchspace

class abo(searchspace):

    def __init__(self, ratio_e=None, step_e=None):

        # call super from searchspace base class
        super().__init__()

        if ratio_e == None:
            print('error: ABC requires that ratio_e be set')
            sys.exit(1)

        if step_e == None:
            print('error: ABC requires that step_e be set')
            sys.exit(1)

        # ABO
        self._ratio_e = 0.0 #
        self._step_e = 0.0 #

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass

