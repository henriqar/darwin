
from .searchspace import searchspace

class gp(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # GP
        self._pReproduction = 0.0 # probability of reproduction
        self._pMutation = 0.0 # probability of mutation
        self._pCrossover = 0.0 # probability of crossover
        self._min_depth = 0.0 # minimum depth of a tree
        self._max_depth = 0.0 # maximum depth of a tree
        self_n_terminals = 0.0 # number of terminals
        self.i_n_functions = 0.0 # number of functions
        self._n_constants = 0.0 # number of constants
        self._function = [] # matrix with the functions' names
        self._terminal = [] # matrix with the terminals' names
        self._constant = [] # matrix with the random constants
        self._T = 0.0 # pointer to the tree

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
        self._tree_fit = 0.0 # fitness of each tree (in GP, the number of agents is different from the number of trees)


