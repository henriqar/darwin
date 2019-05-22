
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

        # struct Pride{
        #     int n_females; /* number of females in a pride */
        #     int n_males; /* number of males in a pride */
        #     Agent **females; /* array of pointers to female lions from a pride */
        #     Agent **males; /* array of pointers to male lions from a pride */
        # }*pride_id; /* array of prides */

class loa(searchspace):

    class pride:

        def __init__(self, nf, nm):
            self._n_females = nf
            self._n_males = nm
            self._females = []
            self._males = []

        @property
        def n_females(self):
            return self._n_females

        @n_females.setter
        def n_females(self, val):
            self._n_females = val

        @property
        def n_males(self):
            return self._n_males

        @n_males.setter
        def n_males(self, val):
            self._n_males = val

        @property
        def females(self):
            return self._females

        @females.setter
        def females(self, val):
            self._females = val

        @property
        def males(self):
            return self._males

        @males.setter
        def males(self, val):
            self._males = val


    def __init__(self, m, n, sex_rate=None, percent_nomad_lions=None,
            roaming_percent=None, mating_probability=None,
            immigrating_rate=None, number_of_pride=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('loa', n))

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

        self._sex_rate = sex_rate # percentage of female lions in each pride
        self._nomad_percent = percent_nomad_lions # percentage of nomad lions in the population
        self._roaming_percent = roaming_percent # percentage of pride territory that will be visited by a male lion
        self._mating_prob = mating_probability # probability of a female mate with male
        self._imigration_rate = immigrating_rate # rate of females in a pride that will become nomads
        self._n_prides = number_of_pride # number of prides

        self._n_female_nomads = round(m*self._nomad_percent*(1-sex_rate)) # number of nomad females
        self._n_male_nomads = round(m*self._nomad_percent*sex_rate) # number of nomad males

        female_nomads = [] # array of pointers to female nomad lions
        male_nomads = [] # array of pointers to male nomad lions
        for i in range(self._n_female_nomads):
            female_nomads.append(agtfct.create_agent('loa'), n)
            male_nomads.append(agtfactory.create_agent('loa'), n) # array of pointers to male nomad lions

        remained_lions = s.m - s.n_female_nomads - s.n_male_nomads;
        lions_each_pride = []
        for i in range(n):
            lions_each_pride.append(np.random.uniform(0, number_of_pride))

        pride_id = []
        for i in range(number_of_pride):

            nf = round(lions_each_pride * (1-sex_rate))
            prd = pride(nf, lions_each_pride - nf)
            pride_id.append(prd)

            for i in range(pride_id[i].n_females):
                prd.females.append(agtfct.create_agent('loa', n))

            for i in range(pride_id[i].n_males):
                prd.males.append(agtfct.create_agent('loa', n))

    def show(self):

        # call super to show basic data
        super.show()

        for i in range(self._m):

            print(f'Agent {i} -> ', end='')
            for j in range(self._n):
                fit = self._a[i].x[j]
                print(f'x[{j}]: {fit}   ', end='')

            print('fitness value: {}'.format(self._a[i].fit))

    def evaluate(self, args):

        for i in range(s.female_nomads):
            s.a[i].evaluate(args)
            s.female_nomads[i].pfit = s.female_nomads[i].fit

        for i in range(s.male_nomads):
            s.a[i].evaluate(args)
            s.male_nomads[i].pfit = s.male_nomads[i].fit

        for i in range(s._n_prides):

            for j in range(s.pride_id[i]._n_females):
                s.pride_id[i].females[j].evaluate(args)
                s.pride_id[i].females[j].pfit = s.pride_id[i].females[j].fit

            for j in range(s.pride_id[i]._n_males):
                s.pride_id[i].males[j].evaluate(args)
                s.pride_id[i].males[j].pfit = s.pride_id[i].males[j].fit


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
