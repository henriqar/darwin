
import datetime
import logging
import math
import numpy as np
import sys
import time

from . import Strategy

from darwin.engine.particles import ParticleUniverse

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

    def initialize(self):
        for p in ParticleUniverse.particles():
            for pos in p.position:
                pos.uniform_random()
            # p.schedule()

    def fitness_evaluation(self):
        for p in ParticleUniverse.particles():
            if p.intermediate < p.fitness:
                p.fitness = p.intermediate


    def generator(self):

        # import pdb; pdb.set_trace()
        particles = ParticleUniverse.particles()
        m = len(particles)
        n = particles[0].n
        data = self.data

        tmp = []
        for p in particles:
            tmp.append(ParticleUniverse.nullitems())

        # create the table of info
        header_output('Iteration', 'Fitness', 'Elapsed')

        for t in range(data.iterations):

            for idx, agent in enumerate(particles):

		# It performs the selectione
                selection = self._roulette_selection(particles, m)

                # perform the crossover
                for p in range(0, math.floor(m/2), 2):

                    crossover_index = np.random.uniform(0, m)
                    for k in range(n):

                        if k < crossover_index:
                            tmp[p][k].holding = particles[selection[p]][k].holding
                            tmp[p+1][k].holding = particles[selection[p+1]][k].holding
                        else:
                            tmp[p][k].holding = particles[selection[p+1]][k].holding
                            tmp[p+1][k].holding = particles[selection[p]][k].holding

                if m % 2 == 0:

                    crossover_index = np.random.uniform(0, n)

                    for k in range(n):

                        if k < crossover_index:
                            tmp[m-1][k].holding = particles[selection[m-1]][k].holding
                        else:
                            tmp[m-1][k].holding = particles[selection[0]][k].holding

		# It performs the mutation
                for j in range(m):

                    if np.random.uniform(0, 1) <= data.mutation_probability:

                        mutation_index = np.random.randint(0, n)
                        particles[j][mutation_index].uniform_random()
                        tmp[idx][mutation_index].holding = particles[j][mutation_index].holding
                        # tmp[idx][mutation_index].holding = particles[j][mutation_index].uniform_random()

                # changes the generation
                # import pdb; pdb.set_trace()
                for j in range(m):
                    for k in range(n):
                        particles[j][k].holding = tmp[j][k].holding

            # get the time elapsed
            start_time = time.time()

            # create a generator using yield
            yield t

            # get the end time
            elapsed_time = time.time() - start_time

            # information output
            info_output(t, data.iterations, ParticleUniverse.global_fitness, datetime.timedelta(seconds=elapsed_time))

        print('\nFINISHED - OK (minimum fitness value {})'.format(ParticleUniverse.global_fitness))

