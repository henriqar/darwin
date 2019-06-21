
import sys
import math

import numpy as np

from darwin.engine.execution._mediator import mediator
from darwin.engine.opt import spfactory as spf

def RouletteSelectionGA(population, k):
    maximum = sum([c.fit for c in population])
    selection_probs = [c.fit/maximum for c in population]
    return np.random.choice(len(population), p=selection_probs, size=k)

class ga(mediator):

    # def execute(self, m, n, engine, func, maps, max_itr):
    def execute(self, engine):

        # extract darwin parametrs from dict
        m = self._dmap['m']
        n = self._dmap['n']
        maps = self._dmap['maps']
        max_itrs = self._dmap['max_itrs']

        # create both factories for agents and searchspace
        # agf.init_factory()
        spf.init_factory()

        # get the searchspace used
        # searchspace = spf.create_searchspace('ga', m, n, engine, maps, self._kwargs)
        searchspace = spf.create_searchspace('ga', self._dmap, engine, self._kwargs)

	# EvaluateSearchSpace(s, _GA_, Evaluate, arg); Initial evaluation of the search space */
        searchspace.evaluate()

        tmp = [[0 for j in range(n)] for i in range(m)]

        for t in range(max_itr):

            print('Running generation {}/{}'.format(t, max_itr))

            for i in range(m):

		# It performs the selectione
                # import pdb; pdb.set_trace()
                selection = RouletteSelectionGA(searchspace.a, m)

                # perform the crossover
                for p in range(0, math.floor(m/2), 2):

                    crossover_index = np.random.uniform(0, m)
                    for k in range(n):

                        if k < crossover_index:
                            tmp[p][k] = searchspace.a[selection[p]].x[k]
                            tmp[p+1][k] = searchspace.a[selection[p+1]].x[k]
                        else:
                            tmp[p][k] = searchspace.a[selection[p+1]].x[k]
                            tmp[p+1][k] = searchspace.a[selection[p]].x[k]

                if m % 2 == 0:

                    crossover_index = np.random.uniform(0, n)

                    for k in range(n):

                        if k < crossover_index:
                            tmp[m-1][k] = searchspace.a[selection[m-1]].x[k]
                        else:
                            tmp[m-1][k] = searchspace.a[selection[0]].x[k]

		# It performs the mutation
                for j in range(m):

                    if np.random.uniform(0, 1) <= searchspace._pMutation:

                        mutation_index = np.random.randint(0, n)
                        _, v = maps[mutation_index]
                        tmp[i][mutation_index] = v.uniform_random_element()

                # changes the generation
                for j in range(m):
                    for k in range(n):
                        searchspace.a[j].x[k] = tmp[j][k]

                # searchspace.evaluate(func, maps)
                searchspace.evaluate()

                # create a generator using yield
                yield

        print('OK (minimum fitness value {})'.format(searchspace.gfit))

        # d = {}
        # # import pdb; pdb.set_trace()
        # for k, v in self._names.items():
        #     d[k] = self._sets[v][0]
        # self._func(*d)

