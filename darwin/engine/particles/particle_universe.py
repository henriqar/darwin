
import collections
import logging
import sys
import contextlib
import os
import copy

from darwin._constants import opt

from .particle import Particle
from .bat_algorithm import BatAlgorithm
from .lion_optimization_algorithm import LionOptimizationAlgorithm
from .migrating_birds_optimization import MigratingBirdsOptimization
from .particle_swarm_optimization import ParticleSwarmOptimization

logger = logging.getLogger(__name__)

@contextlib.contextmanager
def securewd():
    savedwd = os.getcwd()
    yield
    os.chdir(savedwd)

class ParticleUniverse():

    # class parameter
    global_fitness = sys.maxsize
    global_position = None
    _function = None

    # class knows which instances exist and index each one by its name
    __instance = -1
    __instances = collections.OrderedDict()
    __nullitems = None

    @classmethod
    def size(cls, n, opt):

        for _ in range(n):
            cls.__factory(opt)

    @classmethod
    def __factory(cls, optm, *args, **kwargs):

        if optm == opt.BatAlgorithm:
            instance = BatAlgorithm()
        elif optm == opt.LionOptimizationAlgorithm:
            instance = LionOptimizationAlgorithm()
        elif optm == opt.MigratingBirdsOptimization:
            instance = MigratingBirdsOptimization()
        elif optm == opt.ParticleSwarmOptimization:
            instance = ParticleSwarmOptimization()
        else:
            instance = Particle()

        cls.__instance += 1
        name = 'particle_{}'.format(cls.__instance)
        instance._name = name
        cls.__instances[name] = instance

    @classmethod
    def set_function(cls, func):
        if not callable(func):
            logger.error('function "{}" not callable'.format(func))
            sys.exit(1)
        cls._function = func

    @classmethod
    def get(cls, name):
        try:
            return cls.__instances[name]
        except KeyError:
            logger.error('particle "{}" was not allocated'.format(name))
            sys.exit(1)

    @classmethod
    def names(cls):
        return tuple(cls.__instances.keys())

    @classmethod
    def particles(cls):
        return tuple(cls.__instances.values())

    @classmethod
    def evaluateall(cls, root, strategy):
        with securewd():
            for name, particle in cls.__instances.items():
                ppath = os.path.join(root, name)
                os.chdir(ppath)
                fitness = cls._function()
                if fitness < 0:
                    logger.error('negative fitness value found: {}'.format(
                        fitness))
                    sys.exit(1)
                particle.intermediate = fitness

        # after evaluating, update global fitness
        strategy.fitness_evaluation()
        cls.__updateglobal()

    @classmethod
    def __updateglobal(cls):
        name = min(cls.__instances.items(), key=lambda x: x[1].fitness)[0]
        cls.global_fitness = cls.__instances[name].fitness
        cls.global_position = copy.deepcopy(cls.__instances[name].position)

    @classmethod
    def set_nullitems(cls, items):
        for _ in items:
            _.holding = 0
        cls.__nullitems = items

    @classmethod
    def nullitems(cls):
        return copy.deepcopy(cls.__nullitems)


