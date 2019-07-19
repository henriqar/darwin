
import datetime
import logging
import math
import numpy as np
import sys
import time

from . import Strategy

logger = logging.getLogger(__name__)

def header_output(iteration, fitness, elapsed_time):
    print(' {:13s} {:20s} {:25s}'.format(
        iteration, fitness, str(elapsed_time)))

def info_output(iteration, max_itrs, fitness, elapsed_time):
    print(' {:<13d} {:<20f} {:<25s}'.format(
        iteration, fitness, str(elapsed_time)))

class GeneticAlgorithm(Strategy):

    def _roulette_selection(self, population, k):
        maximum = sum([c.fitness for c in population])
        selection_probs = [c.fitness/maximum for c in population]
        return np.random.choice(len(population), p=selection_probs, size=k)

    def initialize(self, particles):
        assert isinstance(particles, (tuple, list))
        for p in particles:
            for pos in p.position:
                pos.uniform_random_element()
            # p.schedule()

    def generator(self, particles):

        # import pdb; pdb.set_trace()
        m = len(particles)
        n = particles[0].n
        data = self.data

        tmp =

        # create the table of info
        header_output('Iteration', 'Fitness', 'Elapsed')

        for t in range(data.iterations):

            for idx, agent in enumerate(particles):

		# It performs the selectione
                selection = self._roulette_selection(particles, len(particles))

                # perform the crossover
                for p in range(0, math.floor(len(particles)/2), 2):

                    crossover_index = np.random.uniform(0, m)
                    for k in range(n):

                        if k < crossover_index:
                            tmp[p][k] = particles[selection[p]][k]
                            tmp[p+1][k] = particles[selection[p+1]][k]
                        else:
                            tmp[p][k] = particles[selection[p+1]][k]
                            tmp[p+1][k] = particles[selection[p]][k]

                if len(particles) % 2 == 0:

                    crossover_index = np.random.uniform(0, n)

                    for k in range(n):

                        if k < crossover_index:
                            tmp[len(particles)-1][k] = particles[selection[len(particles)-1]][k]
                        else:
                            tmp[len(particles)-1][k] = particles[selection[0]][k]

		# It performs the mutation
                for j in range(m):

                    if np.random.uniform(0, 1) <= data.mutation_probability:

                        mutation_index = np.random.randint(0, n)
                        tmp[idx][mutation_index] = particles[j][mutation_index].uniform_random_element()

                # changes the generation
                import pdb; pdb.set_trace()
                for j in range(m):
                    for k in range(n):
                        particles[j][k].holding = tmp[j][k]

            # get the time elapsed
            start_time = time.time()

            # create a generator using yield
            yield t

            # get the end time
            elapsed_time = time.time() - start_time

            # information output
            info_output(t, iterations, searchspace.gfit, datetime.timedelta(seconds=elapsed_time))

        print('\nFINISHED - OK (minimum fitness value {})'.format(searchspace.gfit))

