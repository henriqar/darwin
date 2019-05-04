
from .searchspace import searchspace

class loa(searchspace):

    def __init__(self):

        # call super from searchspace base class
        super().__init__()

        # LOA
        self._sex_rate = 0.0 # percentage of female lions in each pride
        self._nomad_percent = 0.0 # percentage of nomad lions in the population
        self._roaming_percent = 0.0 # percentage of pride territory that will be visited by a male lion
        self._mating_prob = 0.0 # probability of a female mate with male
        self._imigration_rate = 0.0 # rate of females in a pride that will become nomads
        self._n_prides = 0.0 # number of prides
        # struct Pride{
        #     int n_females; /* number of females in a pride */
        #     int n_males; /* number of males in a pride */
        #     Agent **females; /* array of pointers to female lions from a pride */
        #     Agent **males; /* array of pointers to male lions from a pride */
        # }*pride_id; /* array of prides */
        self._n_female_nomads = 0.0 # number of nomad females
        self._n_male_nomads = 0.0 # number of nomad males
        # Agent **female_nomads = 0.0 # array of pointers to female nomad lions
        # Agent **male_nomads = 0.0 # array of pointers to male nomad lions


    def show(self):
        pass

    def evaluate(self):
        pass

    def check(self):
        pass
