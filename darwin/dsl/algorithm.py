
class algorithm():

    def __init__(self, opt_alg):

        # create the dictionary to hold all sets
        # each set will be indexed by and id, created automatically
        self._parameter_sets = {}

        # define the auto incremented parameter id
        self._param_id = 0

        # create the list of exclusive groups
        self._exclusive_groups = []

        # optimization algorithms supported
        self._algorithms = ('abc', 'abo', 'ba', 'bha', 'bsa', 'bso', 'cs', 'de',
                           'fa', 'fpa', 'ga', 'gp', 'hs', 'jade', 'loa', 'mbo',
                           'opt', 'pso', 'sa', 'wca')

        if opt_alg not in self._algorithms:
            raise ValueError('value for opt_alg not recognized')
        else:
            self.opt_alg = opt_alg

    def add_parameter(self, param):

        if isinstance(param, tuple):
            # force mapparam to be tuple, not modifyable
            self._parameter_sets[self._param_id] = set(param)
            self._param_id += 1
            return self._param_id - 1
        else:
            raise TypeError("map parameter must be a tuple type")

    def add_exclusive_group(self, *groups):

        for group in groups:

            # verify if id of grouo matches the tuple expected
            if not isinstance(group, tuple):
                raise TypeError('group descriptor "{}" received not recognized'.format(group))
            else:

                self._exclusive_groups.append(group)



