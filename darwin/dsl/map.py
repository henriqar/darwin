
import itertools
import copy

import numpy as np

class Map(tuple):

    def __new__(self, data):
        try:
            it = iter(data)
        except TypeError :
            raise
        else:
            return tuple.__new__(Map, data)

    @property
    def lb(self):
        return 0

    @property
    def ub(self):
        return len(self)-1

    def uniform_random_element(self, discrete=True):
        if discrete:
            return np.random.randint(0, len(self))
        else:
            return np.random.uniform(0, len(self))

    def gaussian_random_element(self):
        return np.random.normal(0, len(self))

    def cauchy_random_element(self):
        return np.random.standard_cauchy(0, len(self))

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

    # def __add__(self, other):
    #     return Map(tuple(self.iterable) + tuple(other.iterable))

    # def __iadd__(self, other):
    #     return Map(self.iterable + (other,))

    # def __radd__(self, other):
    #     return Map(other.iterable + self.iterable)

    # def __sub__(self, other):
    #     pass

    # def __isub__(self, other):
    #     pass

    # def __rsub__(self, other):
    #     pass

    # def __mul__(self, other):
    #     return Map(tuple(itertools.product(self.iterable, other.iterable)))

    # def __imul__(self, other):
    #     return Map(tuple(itertools.product(self.iterable, (other,))))

    # def __rmul__(self, other):
    #     return Map(tuple(itertools.product(other.iterable, self.iterable)))

    # def __div__(self, other):
    #     pass

    # def __idiv__(self, other):
    #     pass

    # def __rdiv__(self, other):
    #     pass


