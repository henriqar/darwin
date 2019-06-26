
import logging
import os
import platform
import sys

from darwin.engine.paramspace import paramspace
from darwin.engine.execution.strategy_factory import strategyfactory

from darwin.engine.execution.executor import executor

from .constants import constants as cnts
from .map import Map

__log = logging.getLogger('darwin')

class algorithm():

    def __init__(self, opt_alg):

        # instantiate and create the project logger
        cmd_handler = logging.StreamHandler()
        file_handler = logging.FileHandler()

        cmd_hanlder.setLevel(logging.DEBUG)
        file_hanlder.setLevel(logging.INFO)

        cmd_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - \
                %(message)s'))
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - \
                %(levelname)s - %(message)s'))

        # add handlers to logger
        __log.addHandler(cmd_handler)
        __log.addHandler(file_handler)

        strategyfactory.init_factory()

        # create paramspace
        self._pspace = paramspace()

        # define the execution engine
        self._executor = cnts.LOCAL

        # optimization algorithms supported
        algorithms = ('abc', 'abo', 'ba', 'bha', 'bsa', 'bso', 'cs', 'de',
                      'fa', 'fpa', 'ga', 'gp', 'hs', 'jade', 'loa', 'mbo',
                      'opt', 'pso', 'sa', 'wca')

        if opt_alg not in algorithms:
            raise ValueError('value for opt_alg not recognized')
        else:
            self._opt_alg = opt_alg

        # define the varibale to hold the function to be minimized
        self._func = None

        # create the dictionary to call the fectories with kwargs
        self._kwargs = {}

    def __repr__(self):
        return "darwin.algorithm(opt={}, paramspace={}, exc_groups={})".format(
                algorithms, self._paramspace, self._exclusive_groups)

    def add_parameter(self, name, param, discrete):

        # use the paramspace instance to handle the creation and managing os
        # searchspaces
        self._pspace.add_param(name=name, param=param, discrete=discrete)

    def add_exclusive_group(self, *groups):

        # use the paramspace instance to handle the creation and managing os
        # searchspaces
        self._pspace.add_exclusive_group(*groups)

    @property
    def function(self, func):

        # save the function to be minimized
        if callable(func):
            self._func = func
        else:
            __log.error('func {} is not a callable object'.format(func))
            sys.exit(1)

    @property
    def exec_engine(self, engine):

        # get the engine to be executed
        self._executor = engine

    @property
    def agents(self, nro_agents):

        # define how many agents to be used
        if nro_agents <= 0:
            __log.error('incorrect number of agents: {}'.format(nro_agents))
            sys.exit(1)
        else:
            self._pspace.m = int(nro_agents)

    @property
    def iterations(self, max_itrs):

        # set max iterations (guarantee no funny stuff here)
        self._max_itrs = int(max_itrs)
        # self._dmap['max_itrs'] = int(max_itrs)

    def start(self):

        if len(self._pspace) == 0:
            __log.error('error: no map specified')
            sys.exit(1)

        if self._func is None:
            __log.error('error: no function to be minimized was specified')
            sys.exit(1)

        # create paramspace and the corresponfding searchspaces to find the
        # optmization
        self._pspace.build()
        searchspaces = self._pspace.create_searchspaces(self._opt_alg)

        # create optimization algorithm execution
        optimization = fct.create_strategy(self._opt_alg, self._dmap, self._kwargs)

        # create executor
        exec_engine = executor(self._func, self._executor, procs=1,
                timeout=None)
        exec_engine.register_strategy(optimization)

        __log.info('Parameters` space comprehends {} tests, executing a subset \
                with {} tests.'.format(self._pspace.combinations,
                    self._paspace.m*self._max_itrs))
        # engine execution
        # opt.execute(engine)

    # from here on we will create all methods to store specific parameters for
    # each type of optimizations

    # ABC specific information ------------------------------------------------

    @property
    def trial_limit(self, limit):
        self._kwargs['trial_limit'] = limit

    # ABO specific information ------------------------------------------------

    @property
    def ratio_e(self, ratio):
        self._kwargs['ratio_e'] = ratio

    @property
    def step_e(self, step):
        self._kwargs['step_e'] = step

    # BA specific information -------------------------------------------------

    @property
    def f_min(self, val):
        self._kwargs['f_min'] = val

    @property
    def f_max(self, val):
        self._kwargs['f_max'] = val

    @property
    def A(self, val):
        self._kwargs['A'] = val

    @property
    def r(self, val):
        self._kwargs['r'] = val

    # BSA specific information ------------------------------------------------

    @property
    def mix_rate(self, val):
        self._kwargs['mix_rate'] = val

    @property
    def F(self, val):
        self._kwargs['F'] = val

    # BSO specific information ------------------------------------------------

    @property
    def k(self, val):
        self._kwargs['k'] = val

    @property
    def p_one_cluster(self, val):
        self._kwargs['p_one_cluster'] = val

    @property
    def p_one_center(self, val):
        self._kwargs['p_one_center'] = val

    @property
    def p_two_centers(self, val):
        self._kwargs['p_two_centers'] = val

    # CS specific information -------------------------------------------------

    @property
    def beta(self, val):
        self._kwargs['beta'] = val

    @property
    def p(self, val):
        self._kwargs['p'] = val

    @property
    def alpha(self, val):
        self._kwargs['alpha'] = val

    # DE specific information -------------------------------------------------

    @property
    def mutation_factor(self, val):
        self._kwargs['mutation_factor'] = val

    @property
    def crossover_probability(self, val):
        self._kwargs['crossover_probabilty'] = val

    # FA specific information -------------------------------------------------

    @property
    def gamma(self, val):
        self._kwargs['gamma'] = val

    # GA specific information -------------------------------------------------

    @property
    def mutation_probability(self, mut_prob):

        if mut_prob >= 0 or mut_prob <= 1:
            self._kwargs['mutation_probability'] = float(mut_prob)
        else:
            print('error: mutation probabilty must be inside range [0,1]')
            sys.exit(1)

    # GP specific information -------------------------------------------------

    @property
    def reproduction_probability(self, val):

        if val >= 0 or val <= 1:
            self._kwargs['reproduction_probability'] = float(val)
        else:
            print('error: reproduction probability must be inside range [0,1]')
            sys.exit(1)

    @property
    def minimum_depth_tree(self, val):
        self._kwargs['minimum_depth_tree'] = val

    @property
    def maximum_depth_tree(self, val):
        self._kwargs['maximum_depth_tree'] = val

    # HS specific information -------------------------------------------------

    @property
    def HMCR(self, val):
        self._kwargs['HMCR'] = val

    @property
    def PAR(self, val):
        self._kwargs['PAR'] = val

    @property
    def PAR_min(self, val):
        self._kwargs['PAR_min'] = val

    @property
    def PAR_max(self, val):
        self._kwargs['PAR_max'] = val

    @property
    def bw(self, val):
        self._kwargs['bw'] = val

    @property
    def bw_min(self, val):
        self._kwargs['bw_min'] = val

    @property
    def bw_max(self, val):
        self._kwargs['bw_max'] = val

    # LOA specific information ------------------------------------------------

    @property
    def sex_rate(self, val):
        self._kwargs['sex_rate'] = val

    @property
    def percent_nomad_lions(self, val):
        self._kwargs['percent_nomad_lions'] = val

    @property
    def roaming_percent(self, val):
        self._kwargs['roaming_percent'] = val

    @property
    def mating_probability(self, val):
        self._kwargs['mating_probability'] = val

    @property
    def immigrating_rate(self, val):
        self._kwargs['immigrating_rate'] = val

    @property
    def number_of_prides(self, val):
        self._kwargs['number_of_pride'] = val

    # MBO specific information ------------------------------------------------

    @property
    def k(self, val):
        self._kwargs['k'] = val

    @property
    def X(self, val):
        self._kwargs['X'] = val

    @property
    def M(self, val):
        self._kwargs['M'] = val

    # PSO specific information ------------------------------------------------

    @property
    def c1(self, val):
        self._kwargs['c1'] = val

    @property
    def c2(self, val):
        self._kwargs['c2'] = val

    @property
    def w(self, val):
        self._kwargs['w'] = val

    @property
    def w_min(self, val):
        self._kwargs['w_min'] = val

    @property
    def w_max(self, val):
        self._kwargs['w_max'] = val

    # SA specific information -------------------------------------------------

    @property
    def initial_temperature(self, val):
        self._kwargs['initial_temperature'] = val

    @property
    def final_temperature(self, val):
        self._kwargs['final_temperature'] = val

    @property
    def cooling_schedule(val):

        if val in ('boltzmann_annealing',):
            self._kwargs['cooling_schedule'] = val
        else:
            print('error: cooling schedule not recognized "{}"'.format(val))
            sys.exit(1)

    # WCA specific information ------------------------------------------------

    @property
    def nsr(self, val):
        self._kwargs['nsr'] = val

    @property
    def dmax(self, val):
        self._kwargs['dmax'] = val


