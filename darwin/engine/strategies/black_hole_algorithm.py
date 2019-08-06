
import datetime
import logging
import math
import numpy as np
import sys
import time
import copy

from . import Strategy
from . import printHeader, printInfo

import darwin.engine.space as universe
import darwin.engine.particles as particles

logger = logging.getLogger(__name__)

class BlackHoleAlgorithm(Strategy):

    def initialize(self):
        for particle in particles.particles():
            particle.coordinate.uniformRandom()
        yield 'initial'

    def evaluation(self):
        for p in particles.particles():
            p.fitness = p.intermediate

    def _innerGlobalEvaluation(self, gfit, gcoord):
        particle = min(particles.particles(), key=lambda x: x.fitness)
        if particle.fitness < gfit:
            new = (particle.fitness, copy.deepcopy(particle.coordinate))
            particle.fitness = gfit
            particle.position(gcoord)
            return new
        return (gfit, gcoord)
        return None

    def algorithm(self):

        m = len(particles.particles())
        lp = particles.particles()
        data = self.data

        # create the table of info
        printHeader('Iteration', 'Fitness', 'Elapsed')

        dimension = universe.dimension()
        for iteration in range(data.iterations):

            summ = 0
            best = particles.getBestCoordinate()
            for p in particles.particles():
                rand = np.random.uniform(0, 1)
                part = p
                p.coordinate = rand * (best - p.coordinate)
                p.coordinate.inbounds()

            start_time = time.time()
            yield iteration
            elapsed_time = time.time() - start_time

            for particle in particles.particles():
                summ += particle.fitness

            bestc = particles.getBestCoordinate()
            radius = particles.getBestFitness()/summ
            for p in particles.particles():
                dist = p.coordinate.euclideanDistance(bestc)
                if dist < radius:
                    p.coordinate.uniformRandom()
                    p.fitness = sys.maxsize

            # information output
            printInfo(iteration,
                    self.data.iterations,
                    particles.getBestFitness(),
                    datetime.timedelta(seconds=elapsed_time))


