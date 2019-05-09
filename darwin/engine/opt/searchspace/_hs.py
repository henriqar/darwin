
from .searchspace import searchspace

class hs(searchspace):

    def __init__(self, HMCR=None, PAR=None, bw=None):

        # call super from searchspace base class
        super().__init__()

        if HMCR == None:
            print('error: HS searchspace requires a "HMCR" be set')
            sys.exit(1)

        if PAR == None:
            print('error: HS searchspace requires a "PAR" be set')
            sys.exit(1)

        if bw == None:
            print('error: HS searchspace requires a "bw" be set')
            sys.exit(1)

        # HS
        self._HMCR = HMCR # harmony memory considering rate
        self._PAR = PAR # pitch adjusting rate
        self._bw = bw # bandwidth


    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
