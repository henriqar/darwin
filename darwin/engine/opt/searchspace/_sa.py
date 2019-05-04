
from .searchspace import searchspace

class sa(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # SA
        self._cooling_schedule_id = 0.0 # identification number of the cooling schedule used on SA
        self._init_temperature = 0.0 # Initial temperature of the system. If it is 0 (zero) or any value below, we will determine it automatically from the number of iterations.
        self._end_temperature = 0.0 # temperature that means the convergence of the algorithm (Generally = 1)
        self._func_param = 0.0 # extra parameter for the cooling schedule functions

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
