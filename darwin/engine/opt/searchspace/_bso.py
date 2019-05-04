
from .searchspace import searchspace

class bso(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # BSO
        self._p_one_cluster = 0.0 # probability of selecting a cluster center
        self._p_one_center = 0.0 # probability of randomly selecting an idea from a probabilistic selected cluster
        self._p_two_centers = 0.0 # probability of of creating a random combination of two probabilistic selected clusters
        self._k = 0.0 # number of neighbours solutions to be considered for MBO or number of clusters for BSO

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
