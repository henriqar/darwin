
from .agent import agent

class pso:

    def __init__(self):

        # call base class init
        super().__init__()

        # PSO
        self._v = [] # velocity
        self._xl = [] # local best

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, v):
        self._v = v

    @property
    def x1(self):
        return self._x1

    @x1.setter
    def x1(self, x1):
        self._x1 = x1


