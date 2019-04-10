
import searchspace

class gasp(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        #define all GA search space variables
        self.prob_repr = 0 # probability of reproduction
        self.prob_mutation = 0 # probability of mutation
        self.prob_cross = 0 # probability of crossover

    class factory():
        def create(self):
            return gasp()

