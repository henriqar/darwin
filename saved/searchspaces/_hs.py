
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class hs(searchspace):

    def __init__(self, m, n, HMCR=None, PAR=None, bw=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('hs', n))

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

        # call super to show basic data
        super.show()

        for i in range(self._m):

            print('Agent {} -> '.format(i), end='')
            for j in range(self._n):
                fit = self._a[i].x[j]
                print('x[{}]: {}   '.format(j, fit), end='')
            print('fitness value: {}'.format(self._a[i].fit))

    def evaluate(self):
        pass

    def check(self):

        if not isinstance(self._HMCR, float):
            print(' -> Harmony Memory Considering Rate undefined')
            return 1
        elif not isinstance(self._PAR, float):
            print(' -> Pitch Adjusting Rate undefined')
            return 1
        elif not isinstance(self._PAR_min, float):
            print(' -> Minimum Pitch Adjusting Rate undefined')
            return 1
        elif not isinstance(self._PAR_max, float):
            print(' -> Maximum Pitch Adjusting Rate undefined')
            return 1
        elif not isinstance(self._bw, float):
            print(' -> Bandwidth undefined')
            return 1
        elif not isinstance(self._bw_min, float):
            print(' -> Minimum Bandwidth undefined')
            return 1
        elif not isinstance(self._bw_max, float):
            print(' -> Maximum Bandwidth undefined')
            return 1
        else:
            return 0
