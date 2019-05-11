
from .searchspace import searchspace

class loa(searchspace):

    def __init__(self, sex_rate=None, percent_nomad_lions=None, roaming_percent=None, mating_probability=None, immigrating_rate=None, number_of_pride=None):

        # call super from searchspace base class
        super().__init__()

        if sex_rate == None:
            print('error: LOA searchspace requires a "sex_rate" be set')
            sys.exit(1)

        if percent_nomad_lions == None:
            print('error: LOA searchspace requires a "percent_nomad_lions" be set')
            sys.exit(1)

        if roaming_percent == None:
            print('error: LOA searchspace requires a "roaming_percent" be set')
            sys.exit(1)

        if mating_probability == None:
            print('error: LOA searchspace requires a "mating_probability" be set')
            sys.exit(1)

        if immigrating_rate == None:
            print('error: LOA searchspace requires a "immigrating_rate" be set')
            sys.exit(1)

        if number_of_pride == None:
            print('error: LOA searchspace requires a "number_of_pride" be set')
            sys.exit(1)

        # LOA
        self._sex_rate = sex_rate # percentage of female lions in each pride
        self._nomad_percent = percent_nomad_lions # percentage of nomad lions in the population
        self._roaming_percent = roaming_percent # percentage of pride territory that will be visited by a male lion
        self._mating_prob = mating_probability # probability of a female mate with male
        self._imigration_rate = immigrating_rate # rate of females in a pride that will become nomads
        self._n_prides = number_of_pride # number of prides
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

        # call super to show basic data
        super.show()

        for i in range(self._m):

            print(f'Agent {i} -> ', end='')
            for j in range(self._n):
                fit = self._a[i].x[j]
                print(f'x[{j}]: {fit}   ', end='')

            print('fitness value: {}'.format(self._a[i].fit))

    def evaluate(self):
        pass

    def check(self):

        if not isinstance(self._sex_rate, float):
            print(' -> Sex rate undefined')
            return 1
        elif not isinstance(self._nomad_percent, float):
            print(' -> Nomad percentage undefined')
            return 1
        elif not isinstance(self._roaming_percent, float):
            print(' -> Roaming percentage undefined')
            return 1
        elif not isinstance(self._mating_prob, float):
            print(' -> Mating probability undefined')
            return 1
        elif not isinstance(self._imigration_rate, float):
            print(' -> Imigration rate undefined')
            return 1
        elif self._n_prides <= 0:
            print(' -> Number of prides not valid')
            return 1
        elif not isinstance(self._pMutation, float):
            print(' -> Mutation probability undefined')
            return 1
        else:
            return 0
