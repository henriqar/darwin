
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

    def format(self):
        if self._mapref.discrete:
            return self._mapref.format(self._holding)
        else:
            return self._holding

    @property
    def holding(self):
        # if self._mapref.discrete:
        #     return self._mapref.format(self._holding)
        # else:
        return self._holding

    @holding.setter
    def holding(self, value):
        secure = value
        if value < self._mapref.lb:
            secure = self._mapref.lb
        elif value > self._mapref.ub:
            secure = self._mapref.ub

        if self._mapref.discrete:
            self._holding = round(secure)
        else:
            self._holding = secure

    def uniform_random(self):
        self.holding = self._mapref.uniform_random_element()

    def gaussian_random(self):
        self.holding = self._mapref.gaussian_random_element()

    def cauchy_random(self):
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

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __pow__(self, other):
        pass

    def __lshift__(self, other):
        pass

    def __rshift__(self, other):
        pass

    def __and__(self, other):
        pass

    def __xor__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __idiv__(self, other):
        pass

    def __ifloordiv__(self, other):
        pass

    def __imod__(self, other):
        pass

    def __ipow__(self, other):
        pass

    def __ilshift__(self, other):
        pass
    def __irshift__(self, other):
        pass
    def __iand__(self, other):
        pass
    def __ixor__(self, other):
        pass
    def __ior__(self, other):
        pass
    def __neg__(self, other):
        pass
    def __pos__(self, other):
        pass
    def __abs__(self, other):
        pass
    def __invert__(self, other):
        pass
    def __complex__(self, other):
        pass
    def __int__(self, other):
        pass
    def __long__(self, other):
        pass
    def __float__(self, other):
        pass
    def __oct__(self, other):
        pass
    def __hex__(self, other):
        pass
    def __lt__(self, other):
        pass
    def __le__(self, other):
        pass
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass
    def __ge__(self, other):
        pass
    def __gt__(self, other):
        pass
