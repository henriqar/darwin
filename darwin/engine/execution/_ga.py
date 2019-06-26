
import sys
import math

import numpy as np

from darwin.engine.paramspace import paramspace
from darwin.engine.execution.strategy import strategy
# from darwin.engine.opt import spfactory as spf

def RouletteSelectionGA(population, k):
    maximum = sum([c.fit for c in population])
    selection_probs = [c.fit/maximum for c in population]
    return np.random.choice(len(population), p=selection_probs, size=k)

class ga(strategy):

    def initializer(self, searchspace):

        # extract darwin parametrs from dict
        m = searchspace.m
        n = searchspace.n
        # max_itrs = self._dmap['max_itrs']

        # create both factories for agents and searchspace
        # agf.init_factory()
        # spf.init_factory()

        # get the searchspace used
        # searchspace = spf.create_searchspace('ga', m, n, engine, maps, self._kwargs)
        # searchspace = spf.create_searchspace('ga', self._dmap, engine, self._kwargs)

	# EvaluateSearchSpace(s, _GA_, Evaluate, arg); Initial evaluation of the search space */
        searchspace.schedule()

    # def execute(self, m, n, engine, func, maps, max_itr):
    def execute_step(self, searchspace, engine):

        # get the pmappings through the sungleton paramsapce
        maps = paramspace()

        # extract darwin parametrs from dict
        m = searchspace.m
        n = searchspace.n
        max_itrs = self._dmap['max_itrs']

        # create both factories for agents and searchspace
        # agf.init_factory()
        # spf.init_factory()

        # get the searchspace used
        # searchspace = spf.create_searchspace('ga', m, n, engine, maps, self._kwargs)
        # searchspace = spf.create_searchspace('ga', self._dmap, engine, self._kwargs)

	# EvaluateSearchSpace(s, _GA_, Evaluate, arg); Initial evaluation of the search space */
        # searchspace.schedule()

        tmp = [ dict.fromkeys(n, 0) for i in range(m)]
        # tmp = [[0 for j in range(n)] for i in range(m)]

        for t in range(max_itr):

            print('Running generation {}/{}'.format(t, max_itr))

            for i in range(m):

		# It performs the selectione
                # import pdb; pdb.set_trace()
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

                        mutation_index = np.random.randint(0, n)
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

