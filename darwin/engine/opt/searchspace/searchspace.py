
import logging

import abc
import sys

from darwin.engine.paramspace import paramspace

from darwin.engine.opt import agtfactory

__log = logging.getLogger('darwin')

class searchspace(abc.ABC):

    def __init__(self, name, engine):
    # def __init__(self, name, dmap, engine):

        if not isinstance(name, str):
            print('searchspace given name not a string')
            sys.exit(1)

        self._name = name
        # common definitions
        self._m = None
        self._n = None

        # self._m = dmap['m'] # number of agents (solutions)
        # self._n = dmap['n'] # number of decision variables

        self._a = [] # array of pointers to agents
        # for i in range(self._m):
        #     self.a.append(agf.create_agent(name, self._n, engine))

        #     for j in self._n:
        #     # for j in range(self._n):
        #         _,v = maps[j]
        #         self.a[i].x[j] = v.uniform_random_element()

        # self._LB = [] # lower boundaries of each decision variable
        # self._UB = [] # upper boundaries of each decision variable
        self._t_g = [] # global best tensor (matrix)
        self._best = 0 # index of the best agent

        self._g = [] # global best agent
        for i in self._n:
            self._g.append(0)

        # global best fitness
        self._gfit = sys.float_info.max

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

    def init_agents(self, m=None):

        # get the mapping parameters
        maps = paramspace()

        # verify if values exist
        if self._n is None:
            __log.error('user must set the "n" iterable containing the parameters\
                    for this searchspace')
            sys.exit(1)

        if m is not None:
            self._m = m
        elif self._m is None:
            __log.error('user must set the "n" iterable containing the parameters\
                    for this searchspace')
            sys.exit(1)

        # reset agent list if called again
        self._a = []

        for i in range(self._m):
            self.a.append(agtfactory.create_agent(self._name, self._n, engine))

            for j in self._n:
            # for j in range(self._n):
                _,v = maps[j]
                self.a[i].x[j] = v.uniform_random_element()

    @property
    def m(self):
        return self._m

    @property
    def n(self):
        return self._n

    @property
    def a(self):
        return self._a

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
