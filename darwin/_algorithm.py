
import datetime
import logging
import numpy as np
import os
import platform
import sys
import time

import darwin.engine.executors as executors
import darwin.engine.strategies as strategies

from darwin._constants import opt, drm
from darwin.engine.paramspace import Paramspace
from darwin.version import __version__

logger = logging.getLogger(__name__)

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

    def __init__(self, opt_alg, log_file='darwin.log'):

        self._data = Algorithm.Data()

        # create paramspace
        self._pspace = Paramspace()

        # define the execution engine
        self._executor = drm.LOCAL

        self._m = 0

        if hasattr(opt, opt_alg):
            self._data.optimization = opt_alg
        else:
            logger.error('unexpected optimization algorithm defined')
            sys.exit(1)

        # create the dictionary to call the fectories with kwargs
        self._kwargs = {}

    def add_parameter(self, name, param, formatter=None, discrete=False):

        # use the paramspace instance to handle the creation and managing os
        # searchspaces
        self._pspace.add_param(name, param, formatter, discrete)

    def add_exclusive_group(self, *groups):

        # use the paramspace instance to handle the creation and managing os
        # searchspaces
        self._pspace.add_exclusive_group(*groups)

    @property
    def function(self):
        return self._data.func

    @function.setter
    def function(self, func):

        # save the function to be minimized
        if callable(func):
            self._data.func = func
        else:
            logger.error('func {} is not a callable object'.format(func))
            sys.exit(1)

    @property
    def exec_engine(self):
        return self._data.executor

    @exec_engine.setter
    def exec_engine(self, executor):
        if not hasattr(drm, executor):
            logger.error('unexpected executor value {}'.format(executor))
            sys.exit(1)
        else:
            self._data.executor = executor

    @property
    def seed(self):
        return np.random.get_state()[1][0]

    @seed.setter
    def seed(self, seed):
        np.random.seed(seed)
        self._data.seed = seed

    @property
    def agents(self):
        return self._pspace.m

    @agents.setter
    def agents(self, nro_agents):

        # define how many agents to be used
        if nro_agents <= 0:
            logger.error('incorrect number of agents: {}'.format(nro_agents))
            sys.exit(1)
        else:
            self._data.m = int(nro_agents)

    @property
    def iterations(self, max_itrs):
        return self._data.iterations

    @iterations.setter
    def iterations(self, max_itrs):
        self._data.iterations = int(max_itrs)

    def start(self, filename='darwin.submit'):

        if len(self._pspace) == 0:
            logger.error('no map specified')
            sys.exit(1)

        required = ('m', 'func', 'executor', 'optimization')
        self._data.hasrequired(required)

        # print and log information
        self.print_data()

        # create paramspace and the corresponfding searchspaces to find the
        # optmization
        self._pspace.build()
        searchspaces = self._pspace.create_searchspaces(self._data)

        for sp in searchspaces:
            sp.init_agents(self._data.m)

        # create optimization algorithm execution
        optimization = strategies.factory(self._data, self._pspace)

        # create executor
        executor = executors.factory(self._data, filename, procs=1,
                timeout=None)
        executor.register_strategy(optimization)

        start_time = time.time()

        executor.execute(searchspaces)

        elapsed_time = time.time() - start_time
        print('\nTotal optimization time: ', datetime.timedelta(
            seconds=elapsed_time))

    def print_data(self):

        print('-'*80)
        print('darwin v{}\n'.format(__version__))

        print('Opt algorithm chosen -> ', self._data.optimization)
        logger.info('Opt algorithm chosen -> ', self._data.optimization)

        print('DRM engine chosen -> {}'.format(self._data.executor))
        logger.info('DRM engine chosen -> {}'.format(self._data.executor))

        print('Max iterations -> {}'.format(self._data.iterations))
        logger.info('Max iterations -> {}'.format(self._data.iterations))

        # print('Seed -> {}\n'.format(self._data.seed))
        # logger.info('Seed -> {}'.format(self.seed))



    # from here on we will create all methods to store specific parameters for
    # each type of optimizations

    # ABC specific information ------------------------------------------------

    @property
    def trial_limit(self):
        self._kwargs['trial_limit']

    @trial_limit.setter
    def trial_limit(self, value):
        self._kwargs['trial_limit'] = value
        self._data.trial_limit = value

    # ABO specific information ------------------------------------------------

    @property
    def ratio_e(self):
        self._kwargs['ratio_e']

    @ratio_e.setter
    def ratio_e(self, value):
        self._kwargs['ratio_e'] = value
        self._data.ratio = value

    @property
    def step_e(self):
        self._kwargs['step_e']

    @step_e.setter
    def step_e(self, value):
        self._kwargs['step_e'] = value
        self._data.step_e = value

    # BA specific information -------------------------------------------------

    @property
    def f_min(self):
        self._kwargs['f_min']

    @f_min.setter
    def f_min(self, value):
        self._kwargs['f_min'] = value
        self._data.f_min = value

    @property
    def f_max(self):
        self._kwargs['f_max']

    @f_max.setter
    def f_max(self, value):
        self._kwargs['f_max'] = value
        self._data.f_max = value

    @property
    def A(self):
        self._kwargs['A']

    @A.setter
    def A(self, value):
        self._kwargs['A'] = value
        self._data.A = value

    @property
    def r(self):
        self._kwargs['r']

    @r.setter
    def r(self, value):
        self._kwargs['r'] = value
        self._data.r = value

    # BSA specific information ------------------------------------------------

    @property
    def mix_rate(self):
        self._kwargs['mix_rate']

    @mix_rate.setter
    def mix_rate(self, value):
        self._kwargs['mix_rate'] = value
        self._data.mix_rate = value

    @property
    def F(self):
        self._kwargs['F']

    @F.setter
    def F(self, value):
        self._kwargs['F'] = value
        self._data.F = value

    # BSO specific information ------------------------------------------------

    @property
    def k(self):
        self._kwargs['k']

    @k.setter
    def k(self, value):
        self._kwargs['k'] = value
        self._data.k = value

    @property
    def p_one_cluster(self):
        self._kwargs['p_one_cluster']

    @p_one_cluster.setter
    def p_one_cluster(self, value):
        self._kwargs['p_one_cluster'] = value
        self._data.p_one_cluster = value

    @property
    def p_one_center(self):
        self._kwargs['p_one_center']

    @p_one_center.setter
    def p_one_center(self, value):
        self._kwargs['p_one_center'] = value
        self._data.p_one_center = value

    @property
    def p_two_centers(self):
        self._kwargs['p_two_centers']

    @p_two_centers.setter
    def p_two_centers(self, value):
        self._kwargs['p_two_centers'] = value
        self._data.p_two_centers = value

    # CS specific information -------------------------------------------------

    @property
    def beta(self):
        self._kwargs['beta']

    @beta.setter
    def beta(self, value):
        self._kwargs['beta'] = value
        self._data.beta = value

    @property
    def p(self):
        self._kwargs['p']

    @p.setter
    def p(self, value):
        self._kwargs['p'] = value
        self._data.p = value

    @property
    def alpha(self):
        self._kwargs['alpha']

    @alpha.setter
    def alpha(self, value):
        self._kwargs['alpha'] = value
        self._data.alpha = value

    # DE specific information -------------------------------------------------

    @property
    def mutation_factor(self):
        self._kwargs['mutation_factor']

    @mutation_factor.setter
    def mutation_factor(self, value):
        self._kwargs['mutation_factor'] = value
        self._data.mutation_factor = value

    @property
    def crossover_probability(self):
        self._kwargs['crossover_probabilty']

    @crossover_probability.setter
    def crossover_probability(self, value):
        self._kwargs['crossover_probabilty'] = value
        self._data.crossover_probability = value

    # FA specific information -------------------------------------------------

    @property
    def gamma(self):
        self._kwargs['gamma']

    @gamma.setter
    def gamma(self, value):
        self._kwargs['gamma'] = value
        self._data.gamma = value

    # GA specific information -------------------------------------------------

    @property
    def mutation_probability(self, mut_prob):
        self._kwargs['mutation_probability']

    @mutation_probability.setter
    def mutation_probability(self, mut_prob):

        if mut_prob >= 0 or mut_prob <= 1:
            self._kwargs['mutation_probability'] = float(mut_prob)
            self._data.mutation_probability = float(mut_prob)
        else:
            print('error: mutation probabilty must be inside range [0,1]')
            sys.exit(1)

    # GP specific information -------------------------------------------------

    @property
    def reproduction_probability(self, val):
        return self._kwargs['reproduction_probability']

    @reproduction_probability.setter
    def reproduction_probability(self, val):

        if val >= 0 or val <= 1:
            self._kwargs['reproduction_probability'] = float(val)
            self._data.reproduction_probability = float(val)
        else:
            print('error: reproduction probability must be inside range [0,1]')
            sys.exit(1)

    @property
    def minimum_depth_tree(self):
        self._kwargs['minimum_depth_tree']

    @minimum_depth_tree.setter
    def minimum_depth_tree(self, value):
        self._kwargs['minimum_depth_tree'] = value
        self._data.minimum_depth_tree = value

    @property
    def maximum_depth_tree(self):
        self._kwargs['maximum_depth_tree']

    @maximum_depth_tree.setter
    def maximum_depth_tree(self, value):
        self._kwargs['maximum_depth_tree'] = value
        self._data.maximum_depth_tree = value

    # HS specific information -------------------------------------------------

    @property
    def HMCR(self):
        self._kwargs['HMCR']

    @HMCR.setter
    def HMCR(self, value):
        self._kwargs['HMCR'] = value
        self._data.HMCR = value

    @property
    def PAR(self):
        self._kwargs['PAR']

    @PAR.setter
    def PAR(self, value):
        self._kwargs['PAR'] = value
        self._data.PAR = value

    @property
    def PAR_min(self):
        self._kwargs['PAR_min']

    @PAR_min.setter
    def PAR_min(self, value):
        self._kwargs['PAR_min'] = value
        self._data.PAR_min = value

    @property
    def PAR_max(self):
        self._kwargs['PAR_max']

    @PAR_max.setter
    def PAR_max(self, value):
        self._kwargs['PAR_max'] = value
        self._data.PAR_max = value

    @property
    def bw(self):
        self._kwargs['bw']

    @bw.setter
    def bw(self, value):
        self._kwargs['bw'] = value
        self._data.bw = value

    @property
    def bw_min(self):
        self._kwargs['bw_min']

    @bw_min.setter
    def bw_min(self, value):
        self._kwargs['bw_min'] = value
        self._data.bw_min = value

    @property
    def bw_max(self):
        self._kwargs['bw_max']

    @bw_max.setter
    def bw_max(self, value):
        self._kwargs['bw_max'] = value
        self._data.bw_max = value

    # LOA specific information ------------------------------------------------

    @property
    def sex_rate(self):
        self._kwargs['sex_rate']

    @sex_rate.setter
    def sex_rate(self, value):
        self._kwargs['sex_rate'] = value
        self._data.sex_rate = value

    @property
    def percent_nomad_lions(self):
        self._kwargs['percent_nomad_lions']

    @percent_nomad_lions.setter
    def percent_nomad_lions(self, value):
        self._kwargs['percent_nomad_lions'] = value
        self._data.percent_nomad_lions = value

    @property
    def roaming_percent(self):
        self._kwargs['roaming_percent']

    @roaming_percent.setter
    def roaming_percent(self, value):
        self._kwargs['roaming_percent'] = value
        self._data.roaming_percent = value

    @property
    def mating_probability(self):
        self._kwargs['mating_probability']

    @mating_probability.setter
    def mating_probability(self, value):
        self._kwargs['mating_probability'] = value
        self._data.mating_probability = value

    @property
    def immigrating_rate(self):
        self._kwargs['immigrating_rate']

    @immigrating_rate.setter
    def immigrating_rate(self, value):
        self._kwargs['immigrating_rate'] = value
        self._data.immigrating_rate = value

    @property
    def number_of_prides(self):
        self._kwargs['number_of_pride']

    @number_of_prides.setter
    def number_of_prides(self, value):
        self._kwargs['number_of_pride'] = value
        self._data.number_of_prides = value

    # MBO specific information ------------------------------------------------

    @property
    def k(self):
        self._kwargs['k']

    @k.setter
    def k(self, value):
        self._kwargs['k'] = value
        self._data.k = value

    @property
    def X(self):
        self._kwargs['X']

    @X.setter
    def X(self, value):
        self._kwargs['X'] = value
        self._data.X = value

    @property
    def M(self):
        self._kwargs['M']

    @M.setter
    def M(self, value):
        self._kwargs['M'] = value
        self._data.M = value

    # PSO specific information ------------------------------------------------

    @property
    def c1(self):
        self._kwargs['c1']

    @c1.setter
    def c1(self, value):
        self._kwargs['c1'] = value
        self._data.c1 = value

    @property
    def c2(self):
        self._kwargs['c2']

    @c2.setter
    def c2(self, value):
        self._kwargs['c2'] = value
        self._data.c2 = value

    @property
    def w(self):
        self._kwargs['w']

    @w.setter
    def w(self, value):
        self._kwargs['w'] = value
        self._data.w = value

    @property
    def w_min(self):
        self._kwargs['w_min']

    @w_min.setter
    def w_min(self, value):
        self._kwargs['w_min'] = value
        self._data.w_min = value

    @property
    def w_max(self):
        self._kwargs['w_max']

    @w_max.setter
    def w_max(self, value):
        self._kwargs['w_max'] = value
        self._data.w_max = value

    # SA specific information -------------------------------------------------

    @property
    def initial_temperature(self):
        self._kwargs['initial_temperature']

    @initial_temperature.setter
    def initial_temperature(self, value):
        self._kwargs['initial_temperature'] = value
        self._data.initial_temperature = value

    @property
    def final_temperature(self):
        self._kwargs['final_temperature']

    @final_temperature.setter
    def final_temperature(self, value):
        self._kwargs['final_temperature'] = value
        self._data.final_temperature = value

    @property
    def cooling_schedule(self, val):
        return self._kwargs['cooling_schedule']

    @cooling_schedule.setter
    def cooling_schedule(self, value):

        if val in ('boltzmann_annealing',):
            self._kwargs['cooling_schedule'] = value
            self._data.boltzmann_annealing = value
        else:
            print('error: cooling schedule not recognized "{}"'.format(value))
            sys.exit(1)

    # WCA specific information ------------------------------------------------

    @property
    def nsr(self):
        self._kwargs['nsr']

    @nsr.setter
    def nsr(self, value):
        self._kwargs['nsr'] = value
        self._data.nsr = value

    @property
    def dmax(self):
        self._kwargs['dmax']

    @dmax.setter
    def dmax(self, value):
        self._kwargs['dmax'] = value
        self._data.dmax = value


