
from .agent import agent

class loa(agent):

    def __init__(self, n):

        # call base class init
        super().__init__(n)

        self._xl = [] # local best
        self._prev_x = []
        for i in range(n):
            self._xl.append(0)
            self._prev_x.append(0)

        self._best_fit = 0.0 # best fitness value so far of the agent (associated with xl)
        self._pfit = 0.0 # fitness value of the previous iteration

    @property
    def prev_x(self):
        return self._prev_x

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



