
import datetime
import logging
import math
import numpy as np
import sys
import time

from . import Strategy

logger = logging.getLogger(__name__)

def RouletteSelectionGA(population, k):
    maximum = sum([c.fit for c in population])
    selection_probs = [c.fit/maximum for c in population]
    return np.random.choice(len(population), p=selection_probs, size=k)

def header_output(iteration, fitness, elapsed_time):
    print(' {:13s} {:20s} {:25s}'.format(
        iteration, fitness, str(elapsed_time)))

def info_output(iteration, max_itrs, fitness, elapsed_time):
    print(' {:<13d} {:<20f} {:<25s}'.format(
        iteration, fitness, str(elapsed_time)))

class Ga(Strategy):

    def initializer(self, searchspace):
        searchspace.schedule()

    def step(self, searchspace):

        # get the pmappings through the sungleton paramsapce
        maps = self._pspace

        # extract darwin parametrs from dict
        m = searchspace.m
        n = searchspace.n
        max_itrs = self._data.iterations

        tmp = [dict.fromkeys(n, 0) for i in range(m)]

        # create the table of info
        header_output('Iteration', 'fitness', 'elapsed')

        for t in range(max_itrs):

            for i in range(m):

		# It performs the selectione
                selection = RouletteSelectionGA(searchspace.a, m)

                # perform the crossover
                for p in range(0, math.floor(m/2), 2):

                    crossover_index = np.random.uniform(0, m)
                    for k in n:

                        if k < crossover_index:
                            tmp[p][k] = searchspace.a[selection[p]].x[k]
                            tmp[p+1][k] = searchspace.a[selection[p+1]].x[k]
                        else:
                            tmp[p][k] = searchspace.a[selection[p+1]].x[k]
                            tmp[p+1][k] = searchspace.a[selection[p]].x[k]

                if m % 2 == 0:

                    crossover_index = np.random.uniform(0, len(n))

                    for idx, k in enumerate(n):

                        if idx < crossover_index:
                            tmp[m-1][k] = searchspace.a[selection[m-1]].x[k]
                        else:
                            tmp[m-1][k] = searchspace.a[selection[0]].x[k]

		# It performs the mutation
                for j in range(m):

                    if np.random.uniform(0, 1) <= searchspace.pMutation:

                        mutation_index = np.random.randint(0, len(n))
                        _, v = maps[mutation_index]
                        tmp[i][mutation_index] = v.uniform_random_element()

                # changes the generation
                for j in range(m):
                    for k in n:
                        searchspace.a[j].x[k] = tmp[j][k]

            searchspace.schedule()

            # get the time elapsed
            start_time = time.time()

            # create a generator using yield
            yield t

            # get the end time
            elapsed_time = time.time() - start_time

            # information output
            info_output(t, max_itrs, searchspace.gfit, datetime.timedelta(seconds=elapsed_time))

        print('\nFINISHED - OK (minimum fitness value {})'.format(searchspace.gfit))

