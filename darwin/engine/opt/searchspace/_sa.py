
from .searchspace import searchspace

class sa(searchspace):

    def __init__(self, initial_temperature=None, final_temperature=None, cooling_schedule=None):

        # call super from searchspace base class
        super().__init__()

        if initial_temperature == None:
            print('error: SA searchspace requires a "initial_temperature" be set')
            sys.exit(1)

        if final_temperature == None:
            print('error: SA searchspace requires a "final_temperature" be set')
            sys.exit(1)

        if cooling_schedule == None:
            print('error: SA searchspace requires a "cooling_schedule" be set')
            sys.exit(1)

        # SA
        self._cooling_schedule_id = cooling_schedule # identification number of the cooling schedule used on SA
        self._init_temperature = initial_temperature # Initial temperature of the system. If it is 0 (zero) or any value below, we will determine it automatically from the number of iterations.
        self._end_temperature = final_temperature # temperature that means the convergence of the algorithm (Generally = 1)
        self._func_param = 0.0 # extra parameter for the cooling schedule functions

    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
