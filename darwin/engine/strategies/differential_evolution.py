
import copy
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

class DifferentialEvolution(Strategy):
    def __init__(self, data):
        self.data = data
        self.prev_features = []

    def initialize(self):
        r = ('mutation_factor', 'crossover_probability')
        self.data.hasrequired(r)

        if particles.total() < 3:
            logger.error('insufficient particles (must be at least 3)')
            sys.exit(1)

        for particle in particles.particles():
            particle.coordinate.uniformRandom()
        yield 'initial'

    def evaluation(self):
        for p, prev in zip(particles.particles(), self.prev_features):
            if p.intermediate < p.fitness:
                p.fitness = p.intermediate
            else:
                p.position(prev)

    def algorithm(self):

        m = particles.total()
        lp = particles.particles()
        data = self.data

        # create the table of info
        printHeader('Iteration', 'Fitness', 'Elapsed')

        dimension = universe.dimension()
        for iteration in range(data.iterations):

            self.prev_features = []
            for i, p in enumerate(particles.particles()):
                self._mutationAndRecombination(p, i, particles.total())

            start_time = time.time()
            yield iteration
            elapsed_time = time.time() - start_time

            # information output
            printInfo(iteration,
                    self.data.iterations,
                    particles.getBestFitness(),
                    datetime.timedelta(seconds=elapsed_time))

    def _mutationAndRecombination(self, particle, index, psize):
        a = index; b = index; c = index; k = index
        self.prev_features.append(particle.copyCoord())

        newc = universe.getOrigin()
        while a == index:
            a = np.random.uniform(0, 1) * (psize - 1)
        while b == index or b == a:
            b = np.random.uniform(0, 1) * (psize - 1)
        while c == index or b == c or c == a:
            c = np.random.uniform(0, 1) * (psize - 1)

        try:
            lp = particles.particles()
            for i in range(universe.dimension()):
                if np.random.uniform(0, 1) < self.data.mutation_factor:
                    newc[i] = particle[i]
                else:
                    newc[i] = lp[math.floor(a)][i] + self.data.mutation_factor * \
                            (lp[math.floor(b)][i] + lp[math.floor(c)][i])
        except:
            aaa = a
            bbb = b
            ccc = c
            import pdb; pdb.set_trace()

        # ensure values are inbound
        newc.inbounds()
        particle.position(newc)







