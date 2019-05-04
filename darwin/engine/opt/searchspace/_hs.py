
from .searchspace import searchspace

class hs(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # HS
        self._HMCR = 0.0 # harmony memory considering rate
        self._PAR = 0.0 # pitch adjusting rate
        self._bw = 0.0 # bandwidth


    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
