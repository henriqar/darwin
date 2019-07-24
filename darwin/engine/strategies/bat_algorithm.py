
import copy
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

class BatAlgorithm(Strategy):
    def __init__(self, data):
        super().__init__(data)
        self.iteration = 0

    def initialize(self):

        r = ('min_frequency', 'max_frequency', 'pulse_rate', 'loudness')
        self.data.hasrequired(r)

        data = self.data
        for p in ParticleUniverse.particles():
            p.v = ParticleUniverse.nullitems()
            for pos in p.position:
                pos.uniform_random()

            p.xl = copy.deepcopy(p.position)
            p.frequency = np.random.uniform(data.min_frequency,
                    data.max_frequency)
            p.pulse_rate = np.random.uniform(0, data.pulse_rate)
            p.loudness = np.random.uniform(0, data.loudness)

    def fitness_evaluation(self):
        for p in ParticleUniverse.particles():
            prob = np.random.uniform(0, 1)
            if p.intermediate < p.fitness and prob < p.loudness:
                p.fitness = p.intermediate
                p.pulse_rate = self.data.pulse_rate * \
                        (1 - math.exp(-0.9*self.iteration))
                p.loudness = self.data.loudness * 0.9
                p.xl = copy.deepcopy(p.position)
            else:
                p.set_position(copy.deepcopy(p.xl))

    def generator(self):

        # extract darwin parametrs from dict
        particles = ParticleUniverse.particles()
        m = len(particles)
        n = particles[0].n
        data = self.data

        # create the table of info
        header_output('Iteration', 'fitness', 'elapsed')

        alpha = 0.9

        for t in range(data.iterations):
            self.iteration = t
            for p in particles:
                self.set_bat_frequency(p)
                self.update_bat_velocity(p, n)

                prob = np.random.uniform(0, 1)

                if prob > p.pulse_rate:
                    g = ParticleUniverse.global_position
                    p.xl = copy.deepcopy(p.position)
                    p.set_position(copy.deepcopy(g))

            # get the time elapsed
            start_time = time.time()

            # create a generator using yield
            yield t

            # get the end time
            elapsed_time = time.time() - start_time

            # information output
            info_output(t, data.iterations, ParticleUniverse.global_fitness,
                    datetime.timedelta(seconds=elapsed_time))

        print('\nFINISHED - OK (minimum fitness value {})'.format(
            ParticleUniverse.global_fitness))

    def update_bat_velocity(self, particle, n):

        data = self.data
        g = ParticleUniverse.global_position
        for j in range(n):
            particle.v[j].holding = particle.v[j].holding +\
                (particle[j].holding - g[j].holding)* particle.frequency

    def set_bat_frequency(self, particle):
        beta = np.random.uniform(0,1)
        data = self.data
        particle.f = data.min_frequency + (data.min_frequency -\
                data.max_frequency) * beta



