
from .agent import agent

class sa(agent):

    def __init__(self):

        # call base class init
        super().__init__()

        # SA
        self._LB = [] # lower boundaries of each decision variable of that agent
        self._UB = [] # upper boundaries of each decision variable of that agent

    @property
    def LB(self):
        return self._LB

    @LB.setter
    def LB(self, LB):
        self._LB = LB

    @property
    def UB(self):
        return self._UB

    @UB.setter
    def UB(self, UB):
        self._UB = UB


