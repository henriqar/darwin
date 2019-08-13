
import collections
import contextlib
import copy
import logging
import re
import sys
import os

from importlib import import_module

from .particle import Particle

__all__ = ['Particle', 'size', 'evaluate', 'particles', 'setEvaluationFunction',
        'getBestFitness', 'getBestCoordinate']

logger = logging.getLogger(__name__)

"""
Define the dictionary with all particles for the otimization problem. It will
define a pool of particles and work using a batch approach for the execution
of the optimization algorithms.
"""
_particle_pool = None

"""
Define the global values used to classify the particles defined in this package
"""
_global_fitness = None
_global_coordinate = None
_global_eval_function = None

@contextlib.contextmanager
def _securewd():
    savedwd = os.getcwd()
    yield
    os.chdir(savedwd)

def init():
    global _particle_pool
    global _global_fitness
    global _global_coordinate
    global _global_eval_function
    _particle_pool = collections.OrderedDict()
    _global_fitness = sys.maxsize
    _global_coordinate = None
    _global_eval_function = None

def size(algorithm, number):
    for _ in range(number):
        _factory(algorithm)

def total():
    return len(_particle_pool.values())

def _factory(optm):
    """
    Factory function to create the desired particle to be used in the
    otimization problem.
    """
    try:
        regex = r'[A-Z][^A-Z]*'
        module = '.' + '_'.join([x.lower() for x in re.findall(regex, optm)])

        exec_ = import_module(module, package='darwin.engine.particles')
        class_ = getattr(exec_, optm)
        instance = class_()
    except ImportError:
        instance = Particle()
    except AttributeError:
        logger.error('desired particle is not a subclass of particle')
        sys.exit(1)

    # global _particle_pool
    _particle_pool[instance.name] = instance

def setEvaluationFunction(func):
    """
    Sets the fitness evaluation function globally to all particles.
    """
    if not callable(func):
        logger.error('function "{}" not callable'.format(func))
        sys.exit(1)
    else:
        global _global_eval_function
        _global_eval_function = func

def evaluate(root, strategy):
    """
    evaluate function evaluates all particles fitness using the users
    provided function.

    evaluate function will evaluate each particle in each individual working
    directory created for them, based on the root directory, using a handle
    to the strategy used in the optimization to let the executor know it
    can apply the evaluation scheme intended to the particle.
    """
    with _securewd():
        logger.info('Iteration Fitness Results:')
        for name, particle in _particle_pool.items():
            ppath = os.path.join(root, name)
            os.chdir(ppath)
            fitness = _global_eval_function()
            if fitness < 0:
                logger.error('negative fitness value found: {}'.format(
                    fitness))
                sys.exit(1)
            particle.intermediate = fitness
            logger.info('\tfitness: {0} coordinate: {1!r}'.format(
                fitness, particle.coordinate))

    # after evaluating, update global fitness
    global _global_fitness
    global _global_coordinate
    strategy.evaluation()
    _global_fitness, _global_coordinate = \
            strategy.globalEvaluation(_global_fitness, _global_coordinate)
    logger.info('\tbest fitness: {0} coordinate: {1!r}'.format(
        _global_fitness, _global_coordinate))

def particles():
    """
    Particles will return a tuple of all particles for this optimization
    script.
    """
    return tuple(_particle_pool.values())

def getBestFitness():
    """
    Return the best fitness of all particles at the moment of calling.
    """
    return _global_fitness

def getBestCoordinate():
    """
    Return the best fitness of all particles at the moment of calling.
    """
    return copy.deepcopy(_global_coordinate)

