
import copy
import logging
import numpy as np

from darwin.dsl import DefaultFormatter

logger = logging.getLogger(__name__)

class Map(tuple):

    def __new__(cls, data, discrete, formatter=DefaultFormatter()):
        try:
            it = iter(data)
        except TypeError :
            raise
        else:
            inst = tuple.__new__(Map, data)
            inst._discrete = discrete

            if formatter is None:
                logger.error('formatter can not be a NoneType')
                sys.exit(1)
            else:
                inst._formatter = formatter
            return inst

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

    def uniform_random_element(self):
        if self._discrete:
            return np.random.randint(0, len(self))
        else:
            return np.random.uniform(self[0], self[-1])

    def gaussian_random_element(self):
        if self._discrete:
            return np.random.normal(0, len(self))
        else:
            return np.random.normal(self[0], self[-1])

    def cauchy_random_element(self):
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

