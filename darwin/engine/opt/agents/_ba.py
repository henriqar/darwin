
from .agent import agent

class ba:

    def __init__(self):

        # call base class init
        super().__init__()

        # BA
        self._f = 0.0 # frequency
        self._r = 0.0 # pulse rate
        self._A = 0.0 # loudness

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, f):
        self._f = f

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r):
        self._r = r

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, A):
        self._A = A


