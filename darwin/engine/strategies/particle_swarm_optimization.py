
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

class ParticleSwarmOptimization(Strategy):

    def initialize(self):

        r = ('c1', 'c2', 'w')
        self.data.hasrequired(r)

        for p in ParticleUniverse.particles():
            p.v = ParticleUniverse.nullitems()
            for pos in p.position:
                pos.uniform_random()

    def fitness_evaluation(self):
        for p in ParticleUniverse.particles():
            if p.intermediate < p.fitness:
                p.fitness = p.intermediate
                p.xl = copy.deepcopy(p.position)

    def generator(self):

        # extract darwin parametrs from dict
        particles = ParticleUniverse.particles()
        m = len(particles)
        n = particles[0].n
        data = self.data

        # create the table of info
        header_output('Iteration', 'fitness', 'elapsed')

        for t in range(data.iterations):
            for p in particles:
                self.update_particle_velocity(p, n)
                self.update_particle_position(p, n)

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

    def update_particle_velocity(self, particle, n):

        r1 = np.random.uniform(0,1)
        r2 = np.random.uniform(0,1)

        data = self.data
        g = ParticleUniverse.global_position
        for j in range(n):
            particle.v[j].holding = data.w*particle.v[j].holding + \
                    data.c1*r1*(particle.xl[j].holding - particle[j].holding) + \
                    data.c2*r2*(g[j].holding - particle[j].holding)

    def update_particle_position(self, particle, n):
        for j in range(n):
            particle[j] = particle[j].holding + particle.v[j].holding



