
import abc

class searchspace(abc.ABC):

    def __init__(self):

        self.nro_agents = 0 # number of agents
        self.decision_var = 0 # number of decision variables
        self.iterations = 0 # number of iterations
        self.agents = [] # list of agents
        self.lb = [] # lower boundary of each decision variable
        self.up = [] # upper boundary of each decision variable
        self.global_best_agent = 0
        self.global_best_tensor = 0
        self.best_agent = 0 # index of best agent
        self.global_best_fitness = 0 # global best fitness
        self.is_int_opt = False # is integer optimization problem
        self.tensor_dimension = 0 # tensor dimension

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def check(self):
        pass
