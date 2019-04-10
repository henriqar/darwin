

class agent:

    def __init__(self):

        # common definitions
        self._n = 0 # define the number of decision variables
        self._x = [] # position
        self._fit = 0 # fitness value
        self._t = [] # tensor

        # PSO
        self._v = [] # velocity
        self._xl = [] # local best

        # AIWPSO, LOA
        self._pfit = 0.0 # fitness value of the previous iteration

        # TensorPSO
        self._t_v = [] # tensor velocity (matrix)
        self._t_xl = [] # tensor local best (matrix)

        # BA
        self._f # frequency
        self._r # pulse rate
        self_.A # loudness

        # MBO
        self._nb = [] # array of pointers to neighbours

        # LOA
        self._prev_x = [] # position (associated with pfit)
        self._best_fit = 0.0 # best fitness value so far of the agent (associated with xl)

        # SA
        elf._LB = [] # lower boundaries of each decision variable of that agent
        self._UB = [] # upper boundaries of each decision variable of that agent

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, n):
        self._n = n

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def fit(self):
        return self._fit

    @fit.setter
    def fit(self, fit):
        self._fit = fit

    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, t):
        self._t = t

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

    @property
    def pfit(self):
        return self._pfit

    @pfit.setter
    def pfit(self, pfit):
        self._pfit = pfit

    @property
    def t_v(self):
        return self._t_v

    @t_v.setter
    def t_v(self, t_v):
        self._t_v = t_v

    @property
    def t_x1(self):
        return self._t_x1

    @t_x1.setter
    def t_x1(self, t_x1):
        self._t_x1 = t_x1

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

    @property
    def nb(self):
        return self._nb

    @nb.setter
    def nb(self, nb):
        self._nb = nb

    @property
    def prev_x(self):
        return self._prev_x

    @prev_x.setter
    def prev_x(self, prev_x):
        self._prev_x = prev_x

    @property
    def best_fit(self):
        return self._best_fit

    @best_fit.setter
    def best_fit(self, best_fit):
        self._best_fit = best_fit

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

    def check_limits(self):
        pass

    def copy(self):
        pass

    def evaluate(self):
        pass
