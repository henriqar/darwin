
import datetime
import logging
import math
import numpy as np
import sys
import time

import darwin.engine.particles as particles

from . import Strategy

from darwin.constants import cooling

logger = logging.getLogger(__name__)

def header_output(iteration, fitness, elapsed_time):
    print(' {:13s} {:20s} {:25s}'.format(
        iteration, fitness, str(elapsed_time)))

def info_output(iteration, max_itrs, fitness, elapsed_time):
    print(' {:<13d} {:<20f} {:<25s}'.format(
        iteration, fitness, str(elapsed_time)))

class SimulatedAnnealing(Strategy):

    def cooling(self, T0, t):
            return T0/math.log(1+t)

    def initialize(self):

        r = ('initial_temperature', 'final_temperature')
        self.data.hasrequired(r)

        if self.data.initial_temperature == 0:
            self.data.initial_temperature = end_temperature * math.log(1 +
                    self.data.iterations)

        for p in ParticleUniverse.particles():
            for pos in p.position:
                pos.uniform_random()

        yield -1

    def fitnessEvaluation(self):
        for p in particles.particles():
            p.fitness = p.intermediate

    def algorithm(self):

        # import pdb; pdb.set_trace()
        particle_list = particles.particles()
        m = len(particle_list)
        n = particle_list[0].n
        data = self.data

        current_temp = self.cooling(data.initial_temperature, )

        # create the table of info
        header_output('Iteration', 'Fitness', 'Elapsed')

        # for t in range(data.iterations):
        t = 1
        while current_temp < data.end_temperature:

            for idx, agent in enumerate(particle_list):

		# It performs the selectione
                selection = self._roulette_selection(particle_list, m)

                # perform the crossover
                for p in range(0, math.floor(m/2), 2):

                    crossover_index = np.random.uniform(0, m)
                    for k in range(n):

                        if k < crossover_index:
                            tmp[p][k].holding = particle_list[selection[p]][k].holding
                            tmp[p+1][k].holding = particle_list[selection[p+1]][k].holding
                        else:
                            tmp[p][k].holding = particle_list[selection[p+1]][k].holding
                            tmp[p+1][k].holding = particle_list[selection[p]][k].holding

                if m % 2 == 0:

                    crossover_index = np.random.uniform(0, n)

                    for k in range(n):

                        if k < crossover_index:
                            tmp[m-1][k].holding = particle_list[selection[m-1]][k].holding
                        else:
                            tmp[m-1][k].holding = particle_list[selection[0]][k].holding

		# It performs the mutation
                for j in range(m):

                    if np.random.uniform(0, 1) <= data.mutation_probability:

                        mutation_index = np.random.randint(0, n)
                        particle_list[j][mutation_index].uniform_random()
                        tmp[idx][mutation_index].holding = particle_list[j][mutation_index].holding

                # changes the generation
                for j in range(m):
                    for k in range(n):
                        particle_list[j][k].holding = tmp[j][k].holding

            start_time = time.time()
            yield t
            elapsed_time = time.time() - start_time

            # information output
            info_output(t, data.iterations, particles.getBestFitness(),
                    datetime.timedelta(seconds=elapsed_time))


