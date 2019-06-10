
import sys

import numpy as np

# from darwin.engine.execution._mediator import mediator
from darwin.engine.execution.local import local

from darwin.engine.opt import agtfactory as agf
from darwin.engine.opt import spfactory as spf

def RouletteSelectionGA(population, k):
    maximum = sum([c.fit for c in population])
    selection_probs = [c.fit/maximum for c in population]
    return [np.random.choice(len(population), p=selection_probs, size=k)]

class ga(local):

    def execute(self, m, n, func, names, sets, max_itr):

        # create both factories for agents and searchspace
        agf.init_factory()
        spf.init_factory()

        # get the searchspace used
        searchspace = spf.create_searchspace('ga', m, n, self._kwargs)

        args = {}
	# EvaluateSearchSpace(s, _GA_, Evaluate, arg); /* Initial evaluation of the search space */
        searchspace.evaluate(func, args)

        tmp = [[0 for j in range(n)] for i in range(m)]

        for t in range(max_itr):

            print('Running generation {}/{}'.format(t, max_itr))

            for i in range(m):

		# It performs the selection
                selection = RouletteSelectionGA(searchspace.a, m)

                # perform the crossover
                for j in range(0, m/2, 2):

                    crossover_index = np.uniform.random(0, m)
                    for k in range(n):

                        if k < crossover_index:
                            tmp[i][k] = s.a[selection[i]].x[k]
                            tmp[i+1][k] = s.a[selection[i+1]].x[k]
                        else:
                            tmp[i][k] = s.a[selection[+1]].x[k]
                            tmp[i+1][k] = s.a[selection[i]].x[k]

                if m % 2 == 0:

                    crossover_index = np.random.uniform(0, n)

                    for k in range(n):

                        if k < crossover_index:
                            tmp[m-1][k] = searchspace.a[selection[m-1]].x[k]
                        else:
                            tmp[m-1][k] = searchspace.a[selection[0]].x[k]

		# It performs the mutation
                for j in range(m):

                    if np.uniform.random(0, 1) <= s._pMutation:

                        mutation_index = np.uniform.random(0, n)
                        tmp[i][mutation_index] = np.uniform.random(
                                searchspace._LB, searchspace._UB)

                # changes the generation
                for j in range(m):
                    for k in range(n):
                        s.a[j].x[k] = tmp[j][k]

                searchspace.evaluate(func, args)

        print('OK (minimum fitness value {})'.format(searchspace.gfit))

        # d = {}
        # # import pdb; pdb.set_trace()
        # for k, v in self._names.items():
        #     d[k] = self._sets[v][0]
        # self._func(*d)

