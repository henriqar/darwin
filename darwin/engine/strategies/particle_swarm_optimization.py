
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

class ParticleSwarmOptimization(Strategy):

    def initialize(self):
        r = ('c1', 'c2', 'w')
        self.data.hasrequired(r)
        for p in particles.particles():
            p.v = universe.getOrigin()
            p.coordinate.uniformRandom()
        yield 'initial'

    def evaluation(self):
        for p in particles.particles():
            if p.intermediate < p.fitness:
                p.fitness = p.intermediate
                p.xl = copy.deepcopy(p.coordinate)

    def algorithm(self):

        # extract darwin parametrs from dict
        data = self.data

        # create the table of info
        printHeader('Iteration', 'fitness', 'elapsed')

        dimension = universe.dimension()
        for iteration in range(self.data.iterations):
            for p in particles.particles():
                self._updateParticleVelocity(p, dimension)
                self._updateParticlePosition(p, dimension)
                p.coordinate.inbounds()

            start_time = time.time()
            yield iteration
            elapsed_time = time.time() - start_time

            # information output
            printInfo(iteration,
                    self.data.iterations,
                    particles.getBestFitness(),
                    datetime.timedelta(seconds=elapsed_time))

    def _updateParticleVelocity(self, particle, n):

        r1 = np.random.uniform(0,1)
        r2 = np.random.uniform(0,1)

        best = particles.getBestCoordinate()
        for j in range(n):
            particle.v[j] = self.data.w*particle.v[j] + \
                    self.data.c1*r1*(particle.xl[j]- particle[j]) + \
                    self.data.c2*r2*(best[j]- particle[j])

    def _updateParticlePosition(self, particle, n):
        particle.coordinate += particle.v



