
import collections
import logging
import sys
import contextlib
import os
import copy

logger = logging.getLogger(__name__)

# @contextlib.contextmanager
# def securewd():
#     savedwd = os.getcwd()
#     yield
#     os.chdir(savedwd)

class Particle():

    # # class parameter
    # global_fitness = sys.maxsize
    # global_position = None
    # _function = None

    # # class knows which instances exist and index each one by its name
    # __instance = -1
    # __instances = collections.OrderedDict()
    # __nulliitems = None

    # @classmethod
    # def set_function(cls, func):
    #     if not callable(func):
    #         logger.error('function "{}" not callable'.format(func))
    #         sys.exit(1)
    #     cls._function = func

    # @classmethod
    # def get(cls, name):
    #     try:
    #         return cls.__instances[name]
    #     except KeyError:
    #         logger.error('particle "{}" was not allocated'.format(name))
    #         sys.exit(1)

    # @classmethod
    # def names(cls):
    #     return tuple(cls.__instances.keys())

    # @classmethod
    # def particles(cls):
    #     return tuple(cls.__instances.values())

    # @classmethod
    # def add_instance(cls, instance):
    #     cls.__instance += 1
    #     name = 'particle_{}'.format(cls.__instance)
    #     cls.__instances[name] = instance
    #     instance._name = name

    # @classmethod
    # def evaluateall(cls, root):
    #     with securewd():
    #         for name, particle in cls.__instances.items():
    #             ppath = os.path.join(root, name)
    #             os.chdir(ppath)
    #             fitness = cls._function()
    #             if fitness < 0:
    #                 logger.error('negative fitness value found: {}'.format(
    #                     fitness))
    #                 sys.exit(1)
    #             particle.intermediate = fitness

    #     # after evaluating, update global fitness
    #     cls.__updateglobal()

    # @classmethod
    # def __updateglobal(cls):
    #     name = min(cls.__instances.items(), key=lambda x: x[1].fitness)[0]
    #     cls.global_fitness = cls.__instances[name].fitness
    #     cls.global_position = copy.deepcopy(cls.__instances[name].position)

    # @classmethod
    # def set_nullitems(cls, items):
    #     cls.__nullitems = items

    # @classmethod
    # def nullitems(cls):
    #     return copy.deepcopy(cls.__nulliitems)

    def __init__(self):

        # objects parameters
        self._name = ''
        self._position = None
        self.intermediate = sys.maxsize
        self.fitness = sys.maxsize

        #################################################################

        self.t = [] # tensor

        # define the internal variables and parameter space
        self._pspace = None

    @property
    def position(self):
        return self._position

    @property
    def name(self):
        return self._name

    @property
    def n(self):
        return len(self._position)

    def __setitem__(self, idx, value):
        self._position[idx].holding = value

    def __getitem__(self, idx):
        return self._position[idx]

    def set_position(self, mapitems):
        self._position = tuple(mapitems)


