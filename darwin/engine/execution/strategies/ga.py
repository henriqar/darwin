
import logging
import sys
import math

import numpy as np

from . import Strategy

_log = logging.getLogger('darwin')

def RouletteSelectionGA(population, k):
    maximum = sum([c.fit for c in population])
    selection_probs = [c.fit/maximum for c in population]
    return np.random.choice(len(population), p=selection_probs, size=k)

class Ga(Strategy):

    def initializer(self, searchspace):

        # extract darwin parametrs from dict
        m = searchspace.m
        n = searchspace.n

        searchspace.schedule()

    def execute_step(self, searchspace):

        # get the pmappings through the sungleton paramsapce
        maps = self._pspace

        # extract darwin parametrs from dict
        m = searchspace.m
        n = searchspace.n
        max_itrs = self._max_itrs

        tmp = [dict.fromkeys(n, 0) for i in range(m)]

        for t in range(max_itrs):

            print('Running generation {}/{}'.format(t+1, max_itrs))

            for i in range(m):

		# It performs the selectione
                selection = RouletteSelectionGA(searchspace.a, m)

                # perform the crossover
                for p in range(0, math.floor(m/2), 2):

                    crossover_index = np.random.uniform(0, m)
                    for k in n:
                    # for k in range(n):

                        if k < crossover_index:
                            tmp[p][k] = searchspace.a[selection[p]].x[k]
                            tmp[p+1][k] = searchspace.a[selection[p+1]].x[k]
                        else:
                            tmp[p][k] = searchspace.a[selection[p+1]].x[k]
                            tmp[p+1][k] = searchspace.a[selection[p]].x[k]

                if m % 2 == 0:

                    # crossover_index = np.random.uniform(0, n)
                    crossover_index = np.random.uniform(0, len(n))

                    # for k in n:
                    for idx, k in enumerate(n):
                    # for k in range(n):

                        # if k < crossover_index:
                        if idx < crossover_index:
                            tmp[m-1][k] = searchspace.a[selection[m-1]].x[k]
                        else:
                            tmp[m-1][k] = searchspace.a[selection[0]].x[k]

		# It performs the mutation
                for j in range(m):

                    if np.random.uniform(0, 1) <= searchspace._pMutation:

                        mutation_index = np.random.randint(0, len(n))
                        # import pdb; pdb.set_trace()
                        _, v = maps[mutation_index]
                        tmp[i][mutation_index] = v.uniform_random_element()

                # changes the generation
                for j in range(m):
                    for k in n:
                    # for k in range(n):
                        searchspace.a[j].x[k] = tmp[j][k]

                # searchspace.schedule(func, maps)
                searchspace.schedule()

                # create a generator using yield
                yield

        print('OK (minimum fitness value {})'.format(searchspace.gfit))

        # d = {}
        # # import pdb; pdb.set_trace()
        # for k, v in self._names.items():
        #     d[k] = self._sets[v][0]
        # self._func(*d)

