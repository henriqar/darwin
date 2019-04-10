
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

        # PSO
        self._w = 0.0 # inertia weight
        self._w_min = 0.0 # lower bound for w - used for adaptive inertia weight
        self._w_max = 0.0 # upper bound for w - used for adaptive inertia weight
        self._c1 = 0.0 # c1 parameter
        self._c2 = 0.0 # c2 parameter

        # BA
        self._f_min = 0.0 # minimum frequency
        self._f_max = 0.0 # maximum frequency
        self._r = 0.0 # pulse rate
        self._A = 0.0 # loudness

        # FPA
        self._beta = 0.0 # used to compute the step based on Levy Flight
        self._p = 0.0 # probability of local pollination

        # FA
        self._alpha 0  # randomized parameter
        self._beta_0 = 0 # attractiveness
        self._gamma = 0 # light absorption

        # GP and GA
        self._pReproduction = 0.0 # probability of reproduction
        self._pMutation = 0.0 # probability of mutation
        self._pCrossover = 0.0 # probability of crossover

        # WCA
        self._nsr = 0.0 # number of rivers
        self._dmax = 0.0 # raining process maximum distance

        # GP
        self._min_depth = 0.0 # minimum depth of a tree
        self._max_depth = 0.0 # maximum depth of a tree
        self_n_terminals = 0.0 # number of terminals
        self.i_n_functions = 0.0 # number of functions
        self._n_constants = 0.0 # number of constants
        self._function = [] # matrix with the functions' names
        self._terminal = [] # matrix with the terminals' names
        self._constant = [] # matrix with the random constants
        self._T = 0.0 # pointer to the tree
        self._tree_fit = 0.0 # fitness of each tree (in GP, the number of agents is different from the number of trees)

        # TGP
        double ***t_constant = 0.0 # matrix with the tensor-based random constants

        # MBO
        self._X = 0.0 # number of neighbour solutions to be shared with the next solution
        self._M = 0.0 # number of tours, i.e., the number of iterations for the leader
        self._leftSide = 0.0 # flag to know which bird will be changed

        # ABC
        self._limit = 0.0 # number of trial limits for each food source

        # HS
        self._HMCR = 0.0 # harmony memory considering rate
        self._PAR = 0.0 # pitch adjusting rate
        self._bw = 0.0 # bandwidth

        # IHS
        self._PAR_min, PAR_max = 0.0 # minimum and maximum pitch adjusting rate
        self._bw_min, bw_max = 0.0 # minimum and maximum bandwidth

        # BSO
        self._p_one_cluster = 0.0 # probability of selecting a cluster center
        self._p_one_center = 0.0 # probability of randomly selecting an idea from a probabilistic selected cluster
        self._p_two_centers = 0.0 # probability of of creating a random combination of two probabilistic selected clusters

        # MBO/BSO
        self._k = 0.0 # number of neighbours solutions to be considered for MBO or number of clusters for BSO

        # LOA
        self._sex_rate = 0.0 # percentage of female lions in each pride
        self._nomad_percent = 0.0 # percentage of nomad lions in the population
        self._roaming_percent = 0.0 # percentage of pride territory that will be visited by a male lion
        self._mating_prob = 0.0 # probability of a female mate with male
        self._imigration_rate = 0.0 # rate of females in a pride that will become nomads
        self._n_prides = 0.0 # number of prides
        struct Pride{
            int n_females; /* number of females in a pride */
            int n_males; /* number of males in a pride */
            Agent **females; /* array of pointers to female lions from a pride */
            Agent **males; /* array of pointers to male lions from a pride */
        }*pride_id; /* array of prides */
        self._n_female_nomads = 0.0 # number of nomad females
        self._n_male_nomads = 0.0 # number of nomad males
        Agent **female_nomads = 0.0 # array of pointers to female nomad lions
        Agent **male_nomads = 0.0 # array of pointers to male nomad lions

        # BSA
        self._mix_rate = 0.0 # controls the number of elements of individuals that will mutate in a trial
        self._F = 0.0 # controls the amplitude of the search-direction matrix (oldS - s)

        # JADE
        self._c = 0.0 # rate of parameter adaptation
        self._p_greediness = 0.0 # determines the greediness of the mutation strategy

        # CoBiDE
        self._pb = 0.0 # probability to execute DE according to the covariance matrix learning
        self._ps = 0.0 # proportion of the individuals chosen from the current population to calculate the covariance matrix

        # ABO
        self._ratio_e = 0.0 #
        self._step_e = 0.0 #

        # DE
        self._mutation_factor; /* Mutation factor */
        self._cross_probability = 0.0

        # SA
        self._cooling_schedule_id = 0.0 # identification number of the cooling schedule used on SA
        self._init_temperature = 0.0 # Initial temperature of the system. If it is 0 (zero) or any value below, we will determine it automatically from the number of iterations.
        self._end_temperature = 0.0 # temperature that means the convergence of the algorithm (Generally = 1)
        self._func_param = 0.0 # extra parameter for the cooling schedule functions

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def check(self):
        pass
