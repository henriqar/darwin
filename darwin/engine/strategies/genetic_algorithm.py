
import datetime
import logging
import math
import numpy as np
import sys
import time

from . import Strategy
from . import printHeader, printInfo

import darwin.engine.space as universe
import darwin.engine.particles as particles

logger = logging.getLogger(__name__)

class GeneticAlgorithm(Strategy):

    def _rouletteSelection(self, population):
        k = len(population)
        maximum = sum([c.fitness for c in population])
        selection_probs = [c.fitness/maximum for c in population]
        return np.random.choice(k, p=selection_probs, size=k)

    def initialize(self):
        r = ('mutation_probability',)
        self.data.hasrequired(r)
        for particle in particles.particles():
            particle.coordinate.uniformRandom()
        yield 'initial'

    def evaluation(self):
        for p in particles.particles():
            if p.intermediate < p.fitness:
                p.fitness = p.intermediate

    def algorithm(self):

        m = len(particles.particles())
        lp = particles.particles()
        data = self.data

        tmp = []
        for _ in particles.particles():
            tmp.append(universe.getOrigin())

        # create the table of info
        printHeader('Iteration', 'Fitness', 'Elapsed')

        dimension = universe.dimension()
        for iteration in range(data.iterations):

            selection = self._rouletteSelection(particles.particles())
            for p in range(0, math.floor(m/2), 2):
                crossover_index = math.floor(np.random.uniform(high=dimension))
                for k in range(dimension):
                    if k < crossover_index:
                        tmp[p][k] = lp[selection[p]][k]
                        tmp[p+1][k] = lp[selection[p+1]][k]
                    else:
                        tmp[p][k] = lp[selection[p+1]][k]
                        tmp[p+1][k] = lp[selection[p]][k]

            if m % 2 == 0:
                cross_index = math.floor(np.random.uniform(high=dimension))
                for k in range(dimension):
                    if k < cross_index:
                        tmp[m-1][k]= lp[selection[m-1]][k]
                    else:
                        tmp[m-1][k]= lp[selection[0]][k]

            # It performs the mutation
            for coord in tmp:
                if np.random.uniform(0, 1) <= data.mutation_probability:
                    index = math.floor(np.random.uniform(high=dimension))
                    coord.uniformRandom(index)

            # changes the generation
            for j in range(m):
                lp[j].position(tmp[j])

            start_time = time.time()
            yield iteration
            elapsed_time = time.time() - start_time

            # information output
            printInfo(iteration,
                    self.data.iterations,
                    particles.getBestFitness(),
                    datetime.timedelta(seconds=elapsed_time))


