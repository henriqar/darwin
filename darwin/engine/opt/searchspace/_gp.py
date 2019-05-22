
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class gp(searchspace):

    def __init__(self, m, n, reproduction_probability=None, minimum_depth_tree=None, maximum_depth_tree=None, n_terminals=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('gp', n))

        if reproduction_probability == None:
            print('error: GP searchspace requires a "reproduction_probability" be set')
            sys.exit(1)

        if minimum_depth_tree == None:
            print('error: GP searchspace requires a "minimum_depth_tree" be set')
            sys.exit(1)

        if maximum_depth_tree == None:
            print('error: GP searchspace requires a "maximum_depth_tree" be set')
            sys.exit(1)

        if n_terminals  == None:
            print('error: GP searchspace requires a "n_terminals" be set')
            sys.exit(1)

        self._pReproduction = reproduction_probability # probability of reproduction
        self._pMutation = float('nan') # probability of mutation
        self._pCrossover = float('nan') # probability of crossover

    # s = CreateSearchSpace(m, n, _GP_, min_depth, max_depth, n_terminals, N_CONSTANTS, n_functions, terminal, constant, function);

        self._min_depth = minimum_depth_tree # minimum depth of a tree
        self._max_depth = maximum_depth_tree # maximum depth of a tree
        self_n_terminals = n_terminals # number of terminals
        self._n_functions = 0.0 # number of functions
        self._n_constants = 0.0 # number of constants
        self._function = [] # matrix with the functions' names
        self._terminal = [] # matrix with the terminals' names
        self._constant = [] # matrix with the random constants
        self._T = 0.0 # pointer to the tree

        self._tree_fit = 0.0 # fitness of each tree (in GP, the number of agents is different from the number of trees)

    def show(self):

        # call super to show basic data
        super.show()

        for i in range(self._m):
            fit = self._a[i].fit
            print(f'Agent {i} -> fitness value: {fit}', end='')

    def evaluate(self):
        pass

    def check(self):

        if not isinstance(self._pMutation, float):
            print(' -> Probability of mutation undefined')
            return 1
        else:
            return 0


