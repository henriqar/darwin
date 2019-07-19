
import copy

from .map import Map

class MapItem():

    def __init__(self, name, mapref):
        self._holding = None
        self._mapref = mapref
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def holding(self):
        if self._mapref.discrete:
            return self._mapref.format(self._holding)
        else:
            return self._holding

    @holding.setter
    def holding(self, value):
        secure = value
        if value < self._mapref.lb:
            secure = self._mapref.lb
        elif value > self._mapref.ub:
            secure = self._mapref.ub
        self._holding = secure

    def uniform_random_element(self):
        self.holding = self._mapref.uniform_random_element()

    def gaussian_random_element(self):
        self.holding = self._mapref.gaussian_random_element()

    def cauchy_random_element(self):
        self.holding = self._mapref.cauchy_random_element()

    # def __copy__(self):
    #     cls = self.__class__
    #     newone = cls.__new__(cls)
    #     newone.__dict__.update(self.__dict__)
    #     return newone

    # def __deepcopy__(self, memo):
    #     cls = self.__class__
    #     newone = cls.__new__(cls)
    #     newone.__dict__.update(self.__dict__)
    #     memo[id(newone)] = newone
    #     for k,v in self.__dict__.items():
    #         setattr(newone, k, copy.deepcopy(v, memo))
    #     return newone
