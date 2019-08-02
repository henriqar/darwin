
import copy
import datetime
import logging
import math
import numpy as np
import sys
import time

import darwin.engine.space as universe
import darwin.engine.particles as particles

from . import Strategy
from . import printHeader, printInfo

logger = logging.getLogger(__name__)

_alpha = 0.9

class BatAlgorithm(Strategy):
    def __init__(self, data):
        super().__init__(data)
        self.iteration = 0

    def initialize(self):
        r = ('min_frequency', 'max_frequency', 'pulse_rate', 'loudness')
        self.data.hasrequired(r)
        data = self.data
        for p in particles.particles():
            p.v = universe.getOrigin()
            p.coordinate.uniformRandom()

            p.last_coordinate = copy.deepcopy(p.coordinate)
            p.pulse_rate = np.random.uniform(high=data.pulse_rate)
            p.loudness = np.random.uniform(high=data.loudness)
            p.frequency = np.random.uniform(data.min_frequency,
                    data.max_frequency)

        yield 'initial'

    def evaluation(self):
        for p in particles.particles():
            prob = np.random.uniform(0, 1)
            if p.intermediate < p.fitness and prob < p.loudness:
                p.fitness = p.intermediate
                p.pulse_rate = self.data.pulse_rate * \
                        (1 - math.exp(-_alpha*self.iteration))
                p.loudness = self.data.loudness * _alpha
                p.last_coordinate = copy.deepcopy(p.coordinate)
            else:
                p.position(p.last_coordinate)

    def algorithm(self):
        printHeader('Iteration', 'fitness', 'elapsed')

        dimension = universe.dimension()
        for iteration in range(self.data.iterations):
            self.iteration = iteration
            for p in particles.particles():
                self._setBatFrequency(p)
                self._updateBatVelocity(p, dimension)
                p.coordinate.inbounds()
                prob = np.random.uniform(0, 1)
                if prob > p.pulse_rate:
                    best = particles.getBestCoordinate()
                    p.last_coordinate = copy.deepcopy(p.coordinate)
                    p.position(best)

            start_time = time.time()
            yield iteration
            elapsed_time = time.time() - start_time

            printInfo(iteration,
                    self.data.iterations,
                    particles.getBestFitness(),
                    datetime.timedelta(seconds=elapsed_time))

    def _updateBatVelocity(self, bat, n):
        best = particles.getBestCoordinate()
        for j in range(n):
            bat.v[j] = bat.v[j] + (bat[j] - best[j])* bat.frequency

    def _setBatFrequency(self, bat):
        bat.frequency = self.data.min_frequency + (self.data.min_frequency -\
                self.data.max_frequency) * np.random.uniform(0, 1)



