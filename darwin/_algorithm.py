
import datetime
import logging
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

    def __init__(self, opt_alg, log_file='darwin.log'):

        # start printing
        print('-'*80)
        print('darwin v{}\n'.format(__version__))

        # create paramspace
        self._pspace = Paramspace()

        # define the execution engine
        self._executor = drm.LOCAL

        self._m = 0

        if hasattr(opt, opt_alg):
            self._opt_alg = opt_alg
            print('Opt algorithm chosen -> ', self._opt_alg)
        else:
            logger.error('unexpected optimization algorithm defined')
            sys.exit(1)

        # define the varibale to hold the function to be minimized
        self._func = None

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
        return self._func

    @function.setter
    def function(self, func):

        # save the function to be minimized
        if callable(func):
            self._func = func
        else:
            logger.error('func {} is not a callable object'.format(func))
            sys.exit(1)

    @property
    def exec_engine(self):
        return self._executor

    @exec_engine.setter
    def exec_engine(self, executor):
        if not hasattr(drm, executor):
            logger.error('unexpected executor value {}'.format(executor))
            sys.exit(1)
        else:
            print('DRM engine chosen -> {}'.format(executor))
            self._executor = executor

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
            self._m = int(nro_agents)

    @property
    def iterations(self, max_itrs):
        return self._max_itrs

    @iterations.setter
    def iterations(self, max_itrs):
        self._max_itrs = int(max_itrs)
        print('Max iterations -> {}'.format(self._max_itrs))

    def start(self, filename='darwin.submit'):

        if len(self._pspace) == 0:
            logger.error('no map specified')
            sys.exit(1)

        if self._func is None:
            logger.error('no function to be minimized was specified')
            sys.exit(1)

        # create paramspace and the corresponfding searchspaces to find the
        # optmization
        self._pspace.build()
        searchspaces = self._pspace.create_searchspaces(self._opt_alg,
                self._kwargs)

        for sp in searchspaces:
            sp.init_agents(self._m, self._pspace)

        # create optimization algorithm execution
        optimization = strategies.factory(self._opt_alg,
                self._max_itrs, self._pspace)

        # create executor
        exec_engine = executors.factory(self._executor, self._func,
                self._executor, filename=filename, procs=1, timeout=None)
        exec_engine.register_strategy(optimization)

        start_time = time.time()

        print('')
        exec_engine.execute(searchspaces)

        elapsed_time = time.time() - start_time
        print('\nTotal optimization time: ', datetime.timedelta(
            seconds=elapsed_time))

    # from here on we will create all methods to store specific parameters for
    # each type of optimizations

    # ABC specific information ------------------------------------------------

    @property
    def trial_limit(self):
        self._kwargs['trial_limit']

    @trial_limit.setter
    def trial_limit(self, limit):
        self._kwargs['trial_limit'] = limit

    # ABO specific information ------------------------------------------------

    @property
    def ratio_e(self):
        self._kwargs['ratio_e']

    @ratio_e.setter
    def ratio_e(self, ratio):
        self._kwargs['ratio_e'] = ratio

    @property
    def step_e(self):
        self._kwargs['step_e']

    @step_e.setter
    def step_e(self, step):
        self._kwargs['step_e'] = step

    # BA specific information -------------------------------------------------

    @property
    def f_min(self):
        self._kwargs['f_min']

    @f_min.setter
    def f_min(self, val):
        self._kwargs['f_min'] = val

    @property
    def f_max(self):
        self._kwargs['f_max']

    @f_max.setter
    def f_max(self, val):
        self._kwargs['f_max'] = val

    @property
    def A(self):
        self._kwargs['A']

    @A.setter
    def A(self, val):
        self._kwargs['A'] = val

    @property
    def r(self):
        self._kwargs['r']

    @r.setter
    def r(self, val):
        self._kwargs['r'] = val

    # BSA specific information ------------------------------------------------

    @property
    def mix_rate(self):
        self._kwargs['mix_rate']

    @mix_rate.setter
    def mix_rate(self, val):
        self._kwargs['mix_rate'] = val

    @property
    def F(self):
        self._kwargs['F']

    @F.setter
    def F(self, val):
        self._kwargs['F'] = val

    # BSO specific information ------------------------------------------------

    @property
    def k(self):
        self._kwargs['k']

    @k.setter
    def k(self, val):
        self._kwargs['k'] = val

    @property
    def p_one_cluster(self):
        self._kwargs['p_one_cluster']

    @p_one_cluster.setter
    def p_one_cluster(self, val):
        self._kwargs['p_one_cluster'] = val

    @property
    def p_one_center(self):
        self._kwargs['p_one_center']

    @p_one_center.setter
    def p_one_center(self, val):
        self._kwargs['p_one_center'] = val

    @property
    def p_two_centers(self):
        self._kwargs['p_two_centers']

    @p_two_centers.setter
    def p_two_centers(self, val):
        self._kwargs['p_two_centers'] = val

    # CS specific information -------------------------------------------------

    @property
    def beta(self):
        self._kwargs['beta']

    @beta.setter
    def beta(self, val):
        self._kwargs['beta'] = val

    @property
    def p(self):
        self._kwargs['p']

    @p.setter
    def p(self, val):
        self._kwargs['p'] = val

    @property
    def alpha(self):
        self._kwargs['alpha']

    @alpha.setter
    def alpha(self, val):
        self._kwargs['alpha'] = val

    # DE specific information -------------------------------------------------

    @property
    def mutation_factor(self):
        self._kwargs['mutation_factor']

    @mutation_factor.setter
    def mutation_factor(self, val):
        self._kwargs['mutation_factor'] = val

    @property
    def crossover_probability(self):
        self._kwargs['crossover_probabilty']

    @crossover_probability.setter
    def crossover_probability(self, val):
        self._kwargs['crossover_probabilty'] = val

    # FA specific information -------------------------------------------------

    @property
    def gamma(self):
        self._kwargs['gamma']

    @gamma.setter
    def gamma(self, val):
        self._kwargs['gamma'] = val

    # GA specific information -------------------------------------------------

    @property
    def mutation_probability(self, mut_prob):
        self._kwargs['mutation_probability']

    @mutation_probability.setter
    def mutation_probability(self, mut_prob):

        if mut_prob >= 0 or mut_prob <= 1:
            self._kwargs['mutation_probability'] = float(mut_prob)
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
        else:
            print('error: reproduction probability must be inside range [0,1]')
            sys.exit(1)

    @property
    def minimum_depth_tree(self):
        self._kwargs['minimum_depth_tree']

    @minimum_depth_tree.setter
    def minimum_depth_tree(self, val):
        self._kwargs['minimum_depth_tree'] = val

    @property
    def maximum_depth_tree(self):
        self._kwargs['maximum_depth_tree']

    @maximum_depth_tree.setter
    def maximum_depth_tree(self, val):
        self._kwargs['maximum_depth_tree'] = val

    # HS specific information -------------------------------------------------

    @property
    def HMCR(self):
        self._kwargs['HMCR']

    @HMCR.setter
    def HMCR(self, val):
        self._kwargs['HMCR'] = val

    @property
    def PAR(self):
        self._kwargs['PAR']

    @PAR.setter
    def PAR(self, val):
        self._kwargs['PAR'] = val

    @property
    def PAR_min(self):
        self._kwargs['PAR_min']

    @PAR_min.setter
    def PAR_min(self):
        self._kwargs['PAR_min']

    @property
    def PAR_max(self):
        self._kwargs['PAR_max']

    @PAR_max.setter
    def PAR_max(self, val):
        self._kwargs['PAR_max'] = val

    @property
    def bw(self):
        self._kwargs['bw']

    @bw.setter
    def bw(self, val):
        self._kwargs['bw'] = val

    @property
    def bw_min(self):
        self._kwargs['bw_min']

    @bw_min.setter
    def bw_min(self, val):
        self._kwargs['bw_min'] = val

    @property
    def bw_max(self):
        self._kwargs['bw_max']

    @bw_max.setter
    def bw_max(self, val):
        self._kwargs['bw_max'] = val

    # LOA specific information ------------------------------------------------

    @property
    def sex_rate(self):
        self._kwargs['sex_rate']

    @sex_rate.setter
    def sex_rate(self, val):
        self._kwargs['sex_rate'] = val

    @property
    def percent_nomad_lions(self):
        self._kwargs['percent_nomad_lions']

    @percent_nomad_lions.setter
    def percent_nomad_lions(self, val):
        self._kwargs['percent_nomad_lions'] = val

    @property
    def roaming_percent(self):
        self._kwargs['roaming_percent']

    @roaming_percent.setter
    def roaming_percent(self, val):
        self._kwargs['roaming_percent'] = val

    @property
    def mating_probability(self):
        self._kwargs['mating_probability']

    @mating_probability.setter
    def mating_probability(self, val):
        self._kwargs['mating_probability'] = val

    @property
    def immigrating_rate(self):
        self._kwargs['immigrating_rate']

    @immigrating_rate.setter
    def immigrating_rate(self, val):
        self._kwargs['immigrating_rate'] = val

    @property
    def number_of_prides(self):
        self._kwargs['number_of_pride']

    @number_of_prides.setter
    def number_of_prides(self, val):
        self._kwargs['number_of_pride'] = val

    # MBO specific information ------------------------------------------------

    @property
    def k(self):
        self._kwargs['k']

    @k.setter
    def k(self, val):
        self._kwargs['k'] = val

    @property
    def X(self):
        self._kwargs['X']

    @X.setter
    def X(self, val):
        self._kwargs['X'] = val

    @property
    def M(self):
        self._kwargs['M']

    @M.setter
    def M(self, val):
        self._kwargs['M'] = val

    # PSO specific information ------------------------------------------------

    @property
    def c1(self):
        self._kwargs['c1']

    @c1.setter
    def c1(self, val):
        self._kwargs['c1'] = val

    @property
    def c2(self):
        self._kwargs['c2']

    @c2.setter
    def c2(self, val):
        self._kwargs['c2'] = val

    @property
    def w(self):
        self._kwargs['w']

    @w.setter
    def w(self, val):
        self._kwargs['w'] = val

    @property
    def w_min(self):
        self._kwargs['w_min']

    @w_min.setter
    def w_min(self, val):
        self._kwargs['w_min'] = val

    @property
    def w_max(self):
        self._kwargs['w_max']

    @w_max.setter
    def w_max(self, val):
        self._kwargs['w_max'] = val

    # SA specific information -------------------------------------------------

    @property
    def initial_temperature(self):
        self._kwargs['initial_temperature']

    @initial_temperature.setter
    def initial_temperature(self, val):
        self._kwargs['initial_temperature'] = val

    @property
    def final_temperature(self):
        self._kwargs['final_temperature']

    @final_temperature.setter
    def final_temperature(self, val):
        self._kwargs['final_temperature'] = val

    @property
    def cooling_schedule(self, val):
        return self._kwargs['cooling_schedule']

    @cooling_schedule.setter
    def cooling_schedule(self, val):

        if val in ('boltzmann_annealing',):
            self._kwargs['cooling_schedule'] = val
        else:
            print('error: cooling schedule not recognized "{}"'.format(val))
            sys.exit(1)

    # WCA specific information ------------------------------------------------

    @property
    def nsr(self):
        self._kwargs['nsr']

    @nsr.setter
    def nsr(self, val):
        self._kwargs['nsr'] = val

    @property
    def dmax(self):
        self._kwargs['dmax']

    @dmax.setter
    def dmax(self, val):
        self._kwargs['dmax'] = val


