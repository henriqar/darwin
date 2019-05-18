
import abc
import sys

class searchspace(abc.ABC):

    def __init__(self, m, n):

        # common definitions
        self._m = m # number of agents (solutions)
        self._n = n # number of decision variables
        self._iterations = 0 # number of iterations for convergence

        self._a = [] # array of pointers to agents
        self._LB = [] # lower boundaries of each decision variable
        self._UB = [] # upper boundaries of each decision variable
        self._g = 0 # global best agent
        self._t_g = [] # global best tensor (matrix)
        self._best = 0 # index of the best agent

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

    @property
    def m(self):
        return self._m

    @property
    def a(self):
        return self._a

    def show(self):
        print('Search space with {} agents and {} decision variables'.format(self._m, self._n))

    @abc.abstractmethod
    def evaluate(self, func, args):
        pass

    @abc.abstractmethod
    def check(self):
        pass
