
import abc
import logging
import sys

_log = logging.getLogger('darwin')

class Agent(abc.ABC):

    def __init__(self, n):

        if not isinstance(n, tuple):
            _log.error('agent must receive an iterable with the params used')

        # common definitions
        self._n = n

        # set the intermediate result for each simulation
        self._intermediate = sys.maxsize

        self._x = [] # position
        # for i in range(n):
        #     self._x.append(0)
        self._x = dict.fromkeys(n, None)

        self._fit = sys.maxsize # fitness value
        self._t = [] # tensor

        # AIWPSO
        self._pfit = 0.0 # fitness value of the previous iteration

        # TensorPSO
        self._t_v = [] # tensor velocity (matrix)
        self._t_xl = [] # tensor local best (matrix)

        # define the executor to be used
        self._executor = None

        self._pspace = None

    def set_pspace(self, pspace):
        self._pspace = pspace

    @property
    def intermediate(self):
        return self._intermediate

    @intermediate.setter
    def intermediate(self, val):
        if not isinstance(val, int) and not isinstance(val, float):
            raise TypeError('expected <int> or <float>, got {} for min '
                'function return'.format(type(val)))
        self._intermediate = val

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

    @abc.abstractmethod
    def check_limits(self):
        pass

    @abc.abstractmethod
    def copy(self):
        pass

    def register_executor(self, executor):

        # register the executor used
        self._executor = executor

    # def evaluate(self, func, maps):
    def schedule(self):

        # set the intermediate before executing
        self._intermediate = sys.maxsize

        args = {}
        for i in self._n:
        # for i in range(self._n):
            k, v = self._pspace[i]
            # k, v = self._maps[i]
            args[k] = v[self._x[i]]

        self._executor.register_job(self, args)
