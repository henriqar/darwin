
import collections
import logging
import sys
import contextlib
import os
import copy

from .particle import Particle

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
    __nulliitems = None

    @classmethod
    def factory(cls, optm, *args, **kwargs):

        try:
            regex = r'[A-Z][^A-Z]*'
            module = '_'.join([x.lower() for x in re.findall(regex, optm)])

            exec_ = import_module('.' +  module, package='darwin.engine.particles')
            class_ = getattr(exec_, optm)

            instance = class_(*args, **kwargs)
        except ImportError:
            instance = Particle(*args, **kwargs)
        except AttributeError:
            raise ImportError('{} is not a child of particle'.format(optm))
        else:
            if not issubclass(class_, Particles):
                raise ImportError('there is no {} particle implemented')

        cls.__instance += 1
        name = 'particle_{}'.format(cls.__instance)
        instance._name = name
        cls.__instances[name] = instance
        return instance

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
    def evaluateall(cls, root):
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
        cls.__updateglobal()

    @classmethod
    def __updateglobal(cls):
        name = min(cls.__instances.items(), key=lambda x: x[1].fitness)[0]
        cls.global_fitness = cls.__instances[name].fitness
        cls.global_position = copy.deepcopy(cls.__instances[name].position)

    @classmethod
    def set_nullitems(cls, items):
        cls.__nullitems = items

    @classmethod
    def nullitems(cls):
        return copy.deepcopy(cls.__nulliitems)


