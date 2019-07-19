
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

class Pso(Strategy):

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
                self.update_particle_velocity(s, i)
                self.update_particle_position(s, i)
                self.check_limits()

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

    def update_particle_velocity(self, searchspace, i):

        r1 = np.random.uniform(0,1)
        r2 = np.random.uniform(0,1)

        s = searchspace
        for j in range(s.n):
            s.a[i].v[j] = s.w*s.a[i].v[j] + s.c1*r1*(s.a[i].xl[j] \
                    - s.a[i].x[j]) + s.c2*r2*(s.g[j] - s.a[i].x[j])

    def update_particle_position(self, searchspace, i):

        s = searchspace
        for j in range(s.n):
            s.a[i].x[j] = s.a[i].x[j] + s.a[i].v[j]



