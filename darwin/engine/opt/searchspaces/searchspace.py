
import abc
import logging
import sys

import darwin.engine.opt.agents as agents

logger = logging.getLogger(__name__)

class Searchspace(abc.ABC):

    def __init__(self, name):

        if not isinstance(name, str):
            logger.error('searchspace given name not a string')
            sys.exit(1)

        # common definitions
        self._name = name
        self._m = None
        self._n = None

        # array of pointers to agents
        self._a = []

        self._pspace = None

        # self._LB = [] # lower boundaries of each decision variable
        # self._UB = [] # upper boundaries of each decision variable
        self._t_g = [] # global best tensor (matrix)
        self._best = 0 # index of the best agent

        # global best fitness and corresponding agent values
        self._gfit = sys.float_info.max
        self._g = []

        self._is_integer_opt = False # integer-valued optimization problem?
        self._tensor_dim = 0 # dimension of the tensor

        # TGP
        # double ***t_constant = 0.0 # matrix with the tensor-based random constants

        # IHS
        self._PAR_min = 0.0
        self._PAR_max = 0.0 # minimum and maximum pitch adjusting rate
        self._bw_min = 0.0
        self._bw_max = 0.0 # minimum and maximum bandwidth

        # CoBiDE
        self._pb = 0.0 # probability to execute DE according to the covariance matrix learning
        self._ps = 0.0 # proportion of the individuals chosen from the current population to calculate the covariance matrix

        # self._min_depth = 0.0 # minimum depth of a tree
        # self._max_depth = 0.0 # maximum depth of a tree
        # self_n_terminals = 0.0 # number of terminals
        # self.i_n_functions = 0.0 # number of functions
        # self._n_constants = 0.0 # number of constants
        # self._function = [] # matrix with the functions' names
        # self._terminal = [] # matrix with the terminals' names
        # self._constant = [] # matrix with the random constants
        # self._T = 0.0 # pointer to the tree

        # self._tree_fit = 0.0 # fitness of each tree (in GP, the number of agents is different from the number of trees)

    def global_fitness(self):

        print('\nBest fitness vector:\n')
        for i in self._n:
            name, _ = self._pspace[i]
            print(name, ':', self._g[i])

    def set_paramspace(self, pspace):
        self._pspace = pspace

    def init_agents(self, m, pspace):

        # get the mapping parameters
        maps = self._pspace

        # verify if values exist
        if self._n is None:
            logger.error('user must set the "n" iterable containing the parameters'
                   'for this searchspace')
            sys.exit(1)

        self._m = m

        # reset agent list if called again
        self._a = []

        for i in range(self._m):
            self.a.append(agents.factory(self._name, self._n))
            self.a[i].set_pspace(pspace)

            for j in self._n:
            # for j in range(self._n):
                _,v = maps[j]
                self.a[i].x[j] = v.uniform_random_element()

        for i in self._n:
            self._g.append(sys.maxsize)

    def register_executor(self, executor):

        if not self._a:
            logger.error('agents must be initialized before assignment')
            sys.exit(1)

        for ag in self._a:
            ag.register_executor(executor)

    @property
    def m(self):
        return self._m

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, val):
        self._n = val

    @property
    def a(self):
        return self._a

    @property
    def gfit(self):
        return self._gfit

    @gfit.setter
    def gfit(self, val):
        return self._gfit

    def show(self):
        print('Search space with {} agents and {} decision variables'\
                .format(self._m, self._n))

    @abc.abstractmethod
    def schedule(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def check(self):
        raise NotImplementedError()
