
import datetime
import logging
import numpy as np
import os
import platform
import sys
import time

import darwin.engine.strategies as strategies
import darwin.engine.executors as executors

from darwin._constants import opt, drm
from darwin.engine.particles import ParticleUniverse
from darwin.engine.spaces import Searchspace
from darwin.version import __version__

logger = logging.getLogger(__name__)

class Setter():
    def __init__(self, func, doc=None):
        self.func = func
        self.__doc__ = doc if doc is not None else func.__doc__
    def __set__(self, obj, value):
        return self.func(obj, value)

class Algorithm():

    class Data():
        """
        """

        def __setattr__(self, name, value):
            self.__dict__[name]=value

        def hasrequired(self, attrs):
            assert all(isinstance(attr, str) for attr in attrs)
            for attr in attrs:
                if attr not in vars(self):
                    logger.error('undefined required value "{}"'.format(attr))
                    sys.exit(1)

    def __init__(self, opt_alg):

        self.data = Algorithm.Data()
        self.data.iterations = 10
        self.data.executor = drm.Local

        self.config = Algorithm.Data()
        self.config.timeout = None
        self.config.parallelism = 3600
        self.config.submitfile = 'darwin.submit'
        self.config.optdir = 'darwin.opt'
        self.config.execdir = 'darwin.exec'

        # create paramspace
        self._searchspace = Searchspace()

        # define the execution engine
        self._executor = drm.Local

        if hasattr(opt, opt_alg):
            self.data.optimization = opt_alg
        else:
            logger.error('unexpected optimization algorithm defined')
            sys.exit(1)

    def add_parameter(self, name, param, formatter=None, discrete=False):

        # use the paramspace instance to handle the creation and managing os
        # searchspaces
        self._searchspace.add_param(name, param, formatter, discrete)

    def add_exclusive_group(self, *groups):

        # use the paramspace instance to handle the creation and managing os
        # searchspaces
        self._searchspace.add_exclusive_group(*groups)

    @Setter
    def function(self, func):
        ParticleUniverse.set_function(func)

    @Setter
    def exec_engine(self, executor):
        if not hasattr(drm, executor):
            logger.error('unexpected executor value {}'.format(executor))
            sys.exit(1)
        else:
            self.data.executor = executor

    @Setter
    def seed(self, seed):
        np.random.seed(seed)

    @Setter
    def particles(self, total):

        # define how many agents to be used
        number = int(total)
        if number <= 0:
            logger.error('incorrect number of particles: {}'.format(number))
            sys.exit(1)
        else:
            ParticleUniverse.size(number, self.data.optimization)

    @Setter
    def iterations(self, max_itrs):
        self.data.iterations = int(max_itrs)

    @Setter
    def submitfile(self, name='darwin.submit'):
        self.config.submitfile = name

    @Setter
    def optdir(self, name):
        self.config.optdir = name

    @Setter
    def job_timeout(self, seconds):
        self.config.timeout = seconds

    @Setter
    def parallel_jobs(self, number):
        self.config.parallelism = number

    def start(self):

        if len(self._searchspace) == 0:
            logger.error('no map specified')
            sys.exit(1)
        else:
            self._searchspace.build()

        # get the seed
        self.data.seed = np.random.get_state()[1][0]

        # create strategy and executor
        algorithm = strategies.factory(self.data.optimization, self.data)
        executor = executors.factory(self.data.executor, self.config)
        executor.set_strategy(algorithm)

        # print and log information
        self.print_data()

        executor.optimize()

    def print_data(self):

        print('-'*80)
        print('darwin v{}\n'.format(__version__))

        print('Opt algorithm chosen -> ', self.data.optimization)
        logger.info('Opt algorithm chosen -> {}'.format(
            self.data.optimization))

        print('DRM engine chosen -> {}'.format(self.data.executor))
        logger.info('DRM engine chosen -> {}'.format(self.data.executor))

        print('Max iterations -> {}'.format(self.data.iterations))
        logger.info('Max iterations -> {}'.format(self.data.iterations))

        print('Seed -> {}\n'.format(self.data.seed))
        logger.info('Seed -> {}'.format(self.seed))

    # ABC specific information ------------------------------------------------

    @Setter
    def trial_limit(self, value):
        self.data.trial_limit = value

    # ABO specific information ------------------------------------------------

    @Setter
    def ratio_e(self, value):
        self.data.ratio = value

    @Setter
    def step_e(self, value):
        self.data.step_e = value

    # BA specific information -------------------------------------------------

    @Setter
    def min_frequency(self, value):
        self.data.min_frequency = value

    @Setter
    def max_frequency(self, value):
        self.data.max_frequency = value

    @Setter
    def loudness(self, value):
        self.data.loudness = value

    @Setter
    def pulse_rate(self, value):
        self.data.pulse_rate = value

    # BSA specific information ------------------------------------------------

    @Setter
    def mix_rate(self, value):
        self.data.mix_rate = value

    @Setter
    def F(self, value):
        self.data.F = value

    # BSO specific information ------------------------------------------------

    @Setter
    def k(self, value):
        self.data.k = value

    @Setter
    def p_one_cluster(self, value):
        self.data.p_one_cluster = value

    @Setter
    def p_one_center(self, value):
        self.data.p_one_center = value

    @Setter
    def p_two_centers(self, value):
        self.data.p_two_centers = value

    # CS specific information -------------------------------------------------

    @Setter
    def beta(self, value):
        self.data.beta = value

    @Setter
    def p(self, value):
        self.data.p = value

    @Setter
    def alpha(self, value):
        self.data.alpha = value

    # DE specific information -------------------------------------------------

    @Setter
    def mutation_factor(self, value):
        self.data.mutation_factor = value

    @Setter
    def crossover_probability(self, value):
        self.data.crossover_probability = value

    # FA specific information -------------------------------------------------

    @Setter
    def gamma(self, value):
        self.data.gamma = value

    # GA specific information -------------------------------------------------

    @Setter
    def mutation_probability(self, mut_prob):

        if mut_prob >= 0 or mut_prob <= 1:
            self.data.mutation_probability = float(mut_prob)
        else:
            logger.error('mutation probabilty must be inside range [0,1]')
            sys.exit(1)

    # GP specific information -------------------------------------------------

    @Setter
    def reproduction_probability(self, val):

        if val >= 0 or val <= 1:
            self.data.reproduction_probability = float(val)
        else:
            logger.error('reproduction probability must be inside range [0,1]')
            sys.exit(1)

    @Setter
    def minimum_depth_tree(self, value):
        self.data.minimum_depth_tree = value

    @Setter
    def maximum_depth_tree(self, value):
        self.data.maximum_depth_tree = value

    # HS specific information -------------------------------------------------

    @Setter
    def HMCR(self, value):
        self.data.HMCR = value

    @Setter
    def PAR(self, value):
        self.data.PAR = value

    @Setter
    def PAR_min(self, value):
        self.data.PAR_min = value

    @Setter
    def PAR_max(self, value):
        self.data.PAR_max = value

    @Setter
    def bw(self, value):
        self.data.bw = value

    @property
    def bw_min(self):
        return self.data.bw_min

    @Setter
    def bw_min(self, value):
        self.data.bw_min = value

    @Setter
    def bw_max(self, value):
        self.data.bw_max = value

    # LOA specific information ------------------------------------------------

    @Setter
    def sex_rate(self, value):
        self.data.sex_rate = value

    @Setter
    def percent_nomad_lions(self, value):
        self.data.percent_nomad_lions = value

    @Setter
    def roaming_percent(self, value):
        self.data.roaming_percent = value

    @Setter
    def mating_probability(self, value):
        self.data.mating_probability = value

    @Setter
    def immigrating_rate(self, value):
        self.data.immigrating_rate = value

    @Setter
    def number_of_prides(self, value):
        self.data.number_of_prides = value

    # MBO specific information ------------------------------------------------

    @Setter
    def k(self, value):
        self.data.k = value

    @Setter
    def X(self, value):
        self.data.X = value

    @Setter
    def M(self, value):
        self.data.M = value

    # PSO specific information ------------------------------------------------

    @Setter
    def c1(self, value):
        self.data.c1 = value

    @Setter
    def c2(self, value):
        self.data.c2 = value

    @Setter
    def w(self, value):
        self.data.w = value

    @Setter
    def w_min(self, value):
        self.data.w_min = value

    @Setter
    def w_max(self, value):
        self.data.w_max = value

    # SA specific information -------------------------------------------------

    @Setter
    def initial_temperature(self, value):
        self.data.initial_temperature = value

    @Setter
    def final_temperature(self, value):
        self.data.final_temperature = value

    @Setter
    def cooling_schedule(self, value):

        if val in ('boltzmann_annealing',):
            self.data.boltzmann_annealing = value
        else:
            logger.error('cooling schedule not recognized "{}"'.format(value))
            sys.exit(1)

    # WCA specific information ------------------------------------------------

    @Setter
    def nsr(self, value):
        self.data.nsr = value

    @Setter
    def dmax(self, value):
        self.data.dmax = value


