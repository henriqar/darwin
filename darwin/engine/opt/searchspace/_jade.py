
from .searchspace import searchspace

class jade(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # JADE
        self._c = 0.0 # rate of parameter adaptation
        self._p_greediness = 0.0 # determines the greediness of the mutation strategy


    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
