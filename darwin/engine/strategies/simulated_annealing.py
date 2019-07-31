
import datetime
import logging
import math
import numpy as np
import sys
import time
import copy

import darwin.engine.particles as particles
import darwin.engine.space as universe

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
    def __init__(self, data):
        super().__init__(data)
        self.init = True
        self.last_coordinate = []
        self.current_temp = 0

    def _cooling(self, T0, t):
            return T0/math.log(1+t)

    def initialize(self):

        r = ('initial_temperature', 'final_temperature')
        self.data.hasrequired(r)

        if self.data.initial_temperature == 0:
            self.data.initial_temperature = end_temperature * math.log(1 +
                    self.data.iterations)
        self.current_temp = self._cooling(self.data.initial_temperature, 1)

        for i, p in enumerate(particles.particles()):
            p.coordinate.uniformRandom()

        pl = particles.particles()
        for v in range(universe.dimension()):
            _, var = universe.variable(v)
            incr = (var.map.ub - var.map.lb)/len(pl)
            pl[0].UB.append(var.map.lb + incr)
            pl[0].LB.append(var.map.lb)
            for i, p in enumerate(pl[1:]):
                p.UB.append(pl[i].UB[v] + incr)
                p.LB.append(pl[i].UB[v])

        yield 'initial'

    def fitnessEvaluation(self):
        if self.init:
            self.init = False
            for p in particles.particles():
                p.fitness = p.intermediate
        else:
            for idx, p in enumerate(particles.particles()):
                if (p.intermediate < p.fitness):
                    p.fitness = p.intermediate
                else:
                    prob = math.exp(-(p.intermediate-p.fitness)/self.current_temp)
                    if prob < np.random.uniform(0,1):
                        p.position(self.last_coordinate[idx])
                    else:
                        p.fitness = p.intermediate

    def algorithm(self):

        # import pdb; pdb.set_trace()
        particle_list = particles.particles()
        m = len(particle_list)
        data = self.data

        # create the table of info
        header_output('Iteration', 'Fitness', 'Elapsed')

        # for t in range(data.iterations):
        t = 1
        # current_temp = self._cooling(data.initial_temperature, t)
        while self.current_temp < data.final_temperature and t < data.iterations:

            t += 1
            self.current_temp = self._cooling(data.initial_temperature, t)

            self.last_coordinate = []
            for idx, p in enumerate(particles.particles()):
                # prev_fit.append(p.fitness)
                self.last_coordinate.append(copy.deepcopy(p.coordinate))

                new_pos = universe.Coordinate()
                for i in range(universe.dimension()):
                    new_pos[i] = np.random.uniform(p.LB[i], p.UB[i])
                p.position(new_pos)

            start_time = time.time()
            yield t-1
            elapsed_time = time.time() - start_time

            # for idx, p in enumerate(particle_list):
            #     if (p.fitness > prev_fit[i]):
            #         prob = math.exp(-(p.fitness-prev_fit[idx])/current_temp)
            #         if prob < np.random.uniform(0,1):
            #             p.fitness = prev_fit[i]
            #             p.position(aux_ptr[i])


            # information output
            info_output(t-1, data.iterations, particles.getBestFitness(),
                    datetime.timedelta(seconds=elapsed_time))


