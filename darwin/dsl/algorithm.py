
import platform
import sys

from darwin.engine import execution as dexec

from .constants import constants as cnts

class algorithm():

    def __init__(self, opt_alg):

        # create the dictionary to hold all sets
        # each set will be indexed by and id, created using the name of the
        # parameter. The parameters will be automatically mapped to a discrete
        # integer value on the parameter_map
        self._parameter_sets = {}
        self._parameter_map = {}

        # define the auto incremented parameter id
        self._param_id = 0

        # create the list of exclusive groups
        self._exclusive_groups = []

        # define the execution engine
        self._engine = cnts.LOCAL

        # optimization algorithms supported
        self._algorithms = ('abc', 'abo', 'ba', 'bha', 'bsa', 'bso', 'cs', 'de',
                           'fa', 'fpa', 'ga', 'gp', 'hs', 'jade', 'loa', 'mbo',
                           'opt', 'pso', 'sa', 'wca')

        if opt_alg not in self._algorithms:
            raise ValueError('value for opt_alg not recognized')
        else:
            self._opt_alg = opt_alg

        # define the varibale to hold the function to be minimized
        self._func = None

        # define the number of agents
        self._nro_agents = 0

        #init max iterations
        self._max_itrs = 0

        # create the dictionary to call the fectories with kwargs
        self._kwargs = {}

    def __repr__(self):
        return "darwin.algorithm(opt={}, param={}, exc_groups={})".format(
                self._algorithms, self._parameter_sets, self._exclusive_groups)

    def add_parameter(self, name=None, param=None, discrete=False):

        if name is None or name == '':
            raise TypeError(f"parameter name must be defined, got '{name}'")

        if isinstance(param, tuple):
            # force mapparam to be tuple, not modifyable
            self._parameter_map[name] = self._param_id
            self._parameter_sets[self._param_id] = set(param)
            self._param_id += 1
            return self._parameter_map[name]
        else:
            raise TypeError("error: map parameter must be a tuple type")

    def add_exclusive_group(self, *groups):

        for group in groups:

            # verify if id of grouo matches the tuple expected
            if not isinstance(group, tuple):
                raise TypeError(f'group descriptor "{group}" not recognized')
            else:
                self._exclusive_groups.append(group)

    def set_function(self, func):

        # save the function to be minimized
        self._func = func

    def set_exec_engine(self, engine=cnts.LOCAL):

        # get the engine to be executed
        self._engine = engine

    def set_agents(self, nro_agents):

        # define how many agnets to be used
        self._nro_agents = int(nro_agents)

    def set_max_iterations(self, max_itrs):

        # set max iterations (guarantee no funny stuff here)
        self._max_itrs = int(max_itrs)

    def start(self):

        if not self._parameter_sets:
            print('error: no parameter set specified')
            sys.exit(1)

        if self._func is None:
            print('error: no function to be minimized was specified')
            sys.exit(1)

        # create the engine to be used in the optimization
        if self._engine == cnts.LOCAL:
            engine = dexec.local.local(self._opt_alg, self._kwargs)
        elif self._engine == cnts.HTCONDOR and platform.system == 'Linux':
            engine = dexec.clustering.clustering(self._opt_alg,self._kwargs)

        # engine config
        engine.set_nro_agents(self._nro_agents)
        engine.execute()

    # from here on we will create all methods to store specific parameters for
    # each type of optimizations

    # ABC specific information ------------------------------------------------

    def set_trial_limit(self, limit):
        self._kwargs['trial_limit'] = limit

    # ABO specific information ------------------------------------------------

    def set_ratio_e(self, ratio):
        self._kwargs['ratio_e'] = ratio

    def set_step_e(self, step):
        self._kwargs['step_e'] = step

    # BA specific information -------------------------------------------------

    def set_f_min(self, val):
        self._kwargs['f_min'] = val

    def set_f_max(self, val):
        self._kwargs['f_max'] = val

    def set_A(self, val):
        self._kwargs['A'] = val

    def set_r(self, val):
        self._kwargs['r'] = val

    # BSA specific information ------------------------------------------------

    def set_mix_rate(self, val):
        self._kwargs['mix_rate'] = val

    def set_F(self, val):
        self._kwargs['F'] = val

    # BSO specific information ------------------------------------------------

    def set_k(self, val):
        self._kwargs['k'] = val

    def set_p_one_cluster(self, val):
        self._kwargs['p_one_cluster'] = val

    def set_p_one_center(self, val):
        self._kwargs['p_one_center'] = val

    def set_p_two_centers(self, val):
        self._kwargs['p_two_centers'] = val

    # CS specific information -------------------------------------------------

    def set_beta(self, val):
        self._kwargs['beta'] = val

    def set_p(self, val):
        self._kwargs['p'] = val

    def set_alpha(self, val):
        self._kwargs['alpha'] = val

    # DE specific information -------------------------------------------------

    def set_mutation_factor(self, val):
        self._kwargs['mutation_factor'] = val

    def set_crossover_probability(self, val):
        self._kwargs['crossover_probabilty'] = val

    # FA specific information -------------------------------------------------

    def set_gamma(self, val):
        self._kwargs['gamma'] = val

    # GA specific information -------------------------------------------------

    def set_mutation_probability(self, mut_prob):

        if mut_prob >= 0 or mut_prob <= 1:
            self._kwargs['mutation_probability'] = float(mut_prob)
        else:
            print('error: mutation probabilty must be inside range [0,1]')
            sys.exit(1)

    # GP specific information -------------------------------------------------

    def set_reproduction_probability(self, val):

        if val >= 0 or val <= 1:
            self._kwargs['reproduction_probability'] = float(val)
        else:
            print('error: reproduction probability must be inside range [0,1]')
            sys.exit(1)

    def set_minimum_depth_tree(self, val):
        self._kwargs['minimum_depth_tree'] = val

    def set_maximum_depth_tree(self, val):
        self._kwargs['maximum_depth_tree'] = val

    # HS specific information -------------------------------------------------

    def set_HMCR(self, val):
        self._kwargs['HMCR'] = val

    def set_PAR(self, val):
        self._kwargs['PAR'] = val

    def set_PAR_min(self, val):
        self._kwargs['PAR_min'] = val

    def set_PAR_max(self, val):
        self._kwargs['PAR_max'] = val

    def set_bw(self, val):
        self._kwargs['bw'] = val

    def set_bw_min(self, val):
        self._kwargs['bw_min'] = val

    def set_bw_max(self, val):
        self._kwargs['bw_max'] = val

    # LOA specific information ------------------------------------------------

    def set_sex_rate(self, val):
        self._kwargs['sex_rate'] = val

    def set_percent_nomad_lions(self, val):
        self._kwargs['percent_nomad_lions'] = val

    def set_roaming_percent(self, val):
        self._kwargs['roaming_percent'] = val

    def set_mating_probability(self, val):
        self._kwargs['mating_probability'] = val

    def set_immigrating_rate(self, val):
        self._kwargs['immigrating_rate'] = val

    def set_number_of_prides(self, val):
        self._kwargs['number_of_pride'] = val

    # MBO specific information ------------------------------------------------

    def set_k(self, val):
        self._kwargs['k'] = val

    def set_X(self, val):
        self._kwargs['X'] = val

    def set_M(self, val):
        self._kwargs['M'] = val

    # PSO specific information ------------------------------------------------

    def set_c1(self, val):
        self._kwargs['c1'] = val

    def set_c2(self, val):
        self._kwargs['c2'] = val

    def set_w(self, val):
        self._kwargs['w'] = val

    def set_w_min(self, val):
        self._kwargs['w_min'] = val

    def set_w_max(self, val):
        self._kwargs['w_max'] = val

    # SA specific information -------------------------------------------------

    def set_initial_temperature(self, val):
        self._kwargs['initial_temperature'] = val

    def set_final_temperature(self, val):
        self._kwargs['final_temperature'] = val

    def set_cooling_schedule(val):

        if val in ('boltzmann_annealing',):
            self._kwargs['cooling_schedule'] = val
        else:
            print(f'error: cooling schedule not recognized "{val}"')
            sys.exit(1)

    # WCA specific information ------------------------------------------------

    def set_nsr(self, val):
        self._kwargs['nsr'] = val

    def set_dmax(self, val):
        self._kwargs['dmax'] = val


