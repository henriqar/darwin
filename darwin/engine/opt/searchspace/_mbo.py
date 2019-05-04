
from .searchspace import searchspace

class mbo(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # MBO
        self._X = 0.0 # number of neighbour solutions to be shared with the next solution
        self._M = 0.0 # number of tours, i.e., the number of iterations for the leader
        self._leftSide = 0.0 # flag to know which bird will be changed
        self._k = 0.0 # number of neighbours solutions to be considered for MBO or number of clusters for BSO

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
