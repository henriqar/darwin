
import abc

class searchspace(abc.ABC):

    def __init__(self):

        # common definitions
        self._m = 0 # number of agents (solutions)
        self._n = 0 # number of decision variables
        self._iterations = 0 # number of iterations for convergence
        self._a = [] # array of pointers to agents
        self._LB = [] # lower boundaries of each decision variable
        self._UB = [] # upper boundaries of each decision variable
        self._g = 0 # global best agent
        self._t_g = [] # global best tensor (matrix)
        self._best = 0 # index of the best agent
        self._gfit = 0 # global best fitness
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

    @abc.abstractmethod
    def show(self):
        pass

    @abc.abstractmethod
    def evaluate(self):
        pass

    @abc.abstractmethod
    def check(self):
        pass
