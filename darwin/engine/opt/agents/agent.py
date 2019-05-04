
class agent:

    def __init__(self):

        # common definitions
        self._n = 0 # define the number of decision variables
        self._x = [] # position
        self._fit = 0 # fitness value
        self._t = [] # tensor

        # AIWPSO
        self._pfit = 0.0 # fitness value of the previous iteration

        # TensorPSO
        self._t_v = [] # tensor velocity (matrix)
        self._t_xl = [] # tensor local best (matrix)

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

    def check_limits(self):
        pass

    def copy(self):
        pass

    def evaluate(self):
        pass
