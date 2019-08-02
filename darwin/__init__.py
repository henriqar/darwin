
import datetime
import logging
import numpy as np
import os
import platform
import sys
import time

import darwin.engine.strategies as strategies
import darwin.engine.executors as executors
import darwin.engine.space as universe
import darwin.engine.particles as particles

from darwin.engine.space import Coordinate

from .constants import drm, opt, cooling
from .version import __version__

"""
Define the import __all__ for the darwin package, limiting what the public
API will be.
"""
__all__ = ['drm', 'opt', 'cooling', 'Algorithm']

"""
Define the root logger and all handlers that will be used: file handler and
a cmd handler.
"""
logger = logging.getLogger()
logger.setLevel(logging.INFO)

_cmd = logging.StreamHandler()
_cmd.setLevel(logging.WARNING)
_cmd.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

_file = logging.FileHandler(filename='darwin.log')
_file.setLevel(logging.INFO)
_file.setFormatter(logging.Formatter('%(asctime)s - %(name)s - '
        '%(levelname)s - %(message)s'))

# add handlers to logger
logger.addHandler(_cmd)
logger.addHandler(_file)

class Setter():
    """
    Create a setter handler so that we do not need to create a property and a
    getter for each aspect n the algorithm that the user will be inputting.
    """
    def __init__(self, func, doc=None):
        self.func = func
    def __set__(self, obj, value):
        return self.func(obj, value)

class Data():
    """
    Data inner class to encapsulate a dictionary of data used for each
    optimiztion algorithm.
    """
    def __setattr__(self, name, value):
        self.__dict__[name]=value

    def hasrequired(self, attrs):
        assert all(isinstance(attr, str) for attr in attrs)
        for attr in attrs:
            if attr not in vars(self):
                logger.error('undefined required value "{}"'.format(attr))
                sys.exit(1)

class Algorithm():
    """
    The optimization algorithm and all requirements to execute it.

    The Algorithm class encapsulates the public API desired for the darwin
    library exposing each algorithm as a optimization problem. The user will
    set all requirements according to the algorithm chosen.
    """

    def __init__(self, algorithm):

        self.data = Data()
        self.data.iterations = 10
        self.data.executor = drm.TaskSpooler

        self.config = Data()
        self.config.timeout = 3600
        self.config.parallelism = 1
        self.config.submitfile = 'darwin.submit'
        self.config.optdir = 'darwin.opt'
        self.config.env = 'darwin.exec'

        # create the solution space
        universe.bigBang()

        if hasattr(opt, algorithm):
            self.data.optimization = algorithm
        else:
            logger.error('unexpected optimization algorithm defined')
            sys.exit(1)

    def addVariable(self, name, mapping, formatter=None, discrete=False):
        """
        Add parameter function will add a new variable to the solution
        universe.

        Add a new variable with its corresponding name, mapping, formatter and
        if it is a discrete variable or not.

        :param name: A string indicating the name of the variable used.
        :param mapping: The map of values for this variable (continuous or
        discrete ones).
        :param formatter: Formatter object to format values, default is
        Formatter.
        :param discrete: indicate if the variable is continuous or discrete.
        """
        if formatter is None:
            universe.addVariable(name, mapping, universe.Formatter(), discrete)
        else:
            universe.addVariable(name, mapping, formatter, discrete)

    def addExclusiveGroup(self, *groups):
        """
        Adds a new exclusive group of variables of the solution space.

        :param *groups: multiple tuple arguments defining mutual exclusive
        variables. This functions expects every tuple to be two variable only,
        indicating that each other cannot happen at the same time.
        """
        universe.addExclusiveGroup(*groups)

    @Setter
    def function(self, func):
        particles.setEvaluationFunction(func)

    @Setter
    def executionEngine(self, executor):
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
            particles.size(self.data.optimization, number)

    @Setter
    def iterations(self, max_itrs):
        self.data.iterations = int(max_itrs)

    @Setter
    def submitFile(self, name='darwin.submit'):
        self.config.submitfile = name

    @Setter
    def optmizationDirectory(self, name):
        self.config.optdir = name

    @Setter
    def jobTimeout(self, seconds):
        self.config.timeout = seconds

    @Setter
    def parallelJobs(self, number):
        self.config.parallelism = number

    def start(self):

        if universe.dimension == 0:
            logger.error('solution universe has no variables')
            sys.exit(1)
        else:
            universe.expand()

        # get the seed
        self.data.seed = np.random.get_state()[1][0]

        # create strategy and executor
        algorithm = strategies.factory(self.data.optimization, self.data)
        executor = executors.factory(self.data.executor, self.config)
        executor.setStrategy(algorithm)

        # print and log information
        self._printData()

        executor.optimize()

    def _printData(self):

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
    def minFrequency(self, value):
        self.data.min_frequency = value

    @Setter
    def maxFrequency(self, value):
        self.data.max_frequency = value

    @Setter
    def loudness(self, value):
        self.data.loudness = value

    @Setter
    def pulseRate(self, value):
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
    def mutationProbability(self, mut_prob):

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
    def initialTemperature(self, value):
        self.data.initial_temperature = value

    @Setter
    def finalTemperature(self, value):
        self.data.final_temperature = value

    # WCA specific information ------------------------------------------------

    @Setter
    def nsr(self, value):
        self.data.nsr = value

    @Setter
    def dmax(self, value):
        self.data.dmax = value

