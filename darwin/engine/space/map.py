
import copy
import logging
import math
import numpy as np
import sys

logger = logging.getLogger(__name__)

class Map(tuple):

    def __new__(cls, data, discrete, formatter):
        try:
            it = iter(data)
        except TypeError :
            logger.error('mapping must be a iterable type')
            sys.exit(1)
        else:
            inst = tuple.__new__(Map, data)
            inst._discrete = discrete
            inst._formatter = formatter
        return inst

    def __copy__(self):
        cls = self.__class__
        newone = cls.__new__(cls, self, self._discrete, self._formatter)
        newone.__dict__.update(self.__dict__)
        return newone

    def __deepcopy__(self, memo):
        cls = self.__class__
        newone = cls.__new__(cls, self, self._discrete, self._formatter)
        newone.__dict__.update(self.__dict__)
        memo[id(newone)] = newone
        for k,v in self.__dict__.items():
            setattr(newone, k, copy.deepcopy(v, memo))
        return newone

    @property
    def lb(self):
        if self._discrete:
            return 0
        else:
            return self[0]

    @property
    def ub(self):
        if self._discrete:
            return len(self)-1
        else:
            return self[-1]

    @property
    def discrete(self):
        return self._discrete

    def format(self, idx):
        if self._discrete:
            return self._formatter.format(self[math.floor(idx)])
        else:
            return self._formatter.format(idx)
            # logger.error('formatter class is used only on discrete maps')
            # sys.exit(1)

    def uniformRandom(self):
        if self._discrete:
            return np.random.uniform(0, len(self))
        else:
            return np.random.uniform(self[0], self[-1])

    def gaussianRandom(self):
        if self._discrete:
            return np.random.normal(0, len(self))
        else:
            return np.random.normal(self[0], self[-1])

    def cauchyRandom(self):
        if self._discrete:
            return np.random.standard_cauchy(0, len(self))
        else:
            return np.random.standard_cauchy(self[0], self[-1])

    # def generate_levy_distribution(self):
    #     pass

    # def euclidean_distance(self):
    #     pass

    # def get_perpendicular_vector(self):
    #     pass

    # def normalize_vector(self):
    #     pass

    # def sort_agent(self):
    #     pass

    # def sort_data_by_val(self):
    #     pass

    # def waive_comment(self):
    #     pass

    # def get_FUNCTION_id(self):
    #     pass

    # def roulette_selection(self):
    #     pass

    # def roultte_selection_ga(self):
    #     pass

