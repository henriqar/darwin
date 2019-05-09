
from .searchspace import searchspace

class ba(searchspace):

    def __init__(self, f_min=None, f_max=None, A=None, r=None):

        # call super from searchspace base class
        super().__init__()

        if f_min == None:
            print('error: BA requires that "f_min" be set')
            sys.exit(1)

        if f_max == None:
            print('error: BA requires that "f_max" be set')
            sys.exit(1)

        if A == None:
            print('error: BA requires that "A" be set')
            sys.exit(1)

        if r == None:
            print('error: BA requires that "r" be set')
            sys.exit(1)

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


