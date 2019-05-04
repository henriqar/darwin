
from .agent import agent

class loa:

    def __init__(self):

        # call base class init
        super().__init__()

        # LOA
        self._prev_x = [] # position (associated with pfit)
        self._best_fit = 0.0 # best fitness value so far of the agent (associated with xl)
        self._pfit = 0.0 # fitness value of the previous iteration

    @property
    def prev_x(self):
        return self._prev_x

    @prev_x.setter
    def prev_x(self, prev_x):
        self._prev_x = prev_x

    @property
    def pfit(self):
        return self._pfit

    @pfit.setter
    def pfit(self, pfit):
        self._pfit = pfit

    @property
    def best_fit(self):
        return self._best_fit

    @best_fit.setter
    def best_fit(self, best_fit):
        self._best_fit = best_fit



