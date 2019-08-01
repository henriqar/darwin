
import copy
import logging
import sys
import math

from operator import add, sub

logger = logging.getLogger(__name__)

class Coordinate():

    # the dimension system must be equal for all coordinates in the problem
    __dimension = 0
    __universe = None

    @classmethod
    def setUniverse(cls, universe):
        cls.__universe = universe
        cls.__dimension = cls.__universe.dimension

    def __init__(self):
        if Coordinate.__dimension == 0:
            logger.error('solution universe must be created before',
                    ' creating any coordinate object')
            sys.exit(1)
        else:
            self._points = [0 for i in range(Coordinate.__dimension)]

    def __getitem__(self, item):
        return self._points[item]

    def __setitem__(self, item, value):
        self._points[item] = value

    def __len__(self):
        return len(self._points)

    def __repr__(self):
        arguments = []
        for i, ref in Coordinate.__universe.axes():
            p = self._points[i]
            arguments.append('{}: {}'.format(ref.name, ref.map.format(p)))
        return '\n'.join(arguments)

    def set(self, points):
        assert isinstance(points, (tuple, list))
        self._points = copy.deepcopy(points)

    def format(self):
        arguments = []
        for i, ref in Coordinate.__universe.axes():
            p = self._points[i]
            arguments.append('-{} {}'.format(ref.name, ref.map.format(p)))
        return ' '.join(arguments)

    def inbounds(self):
        for point, ref in Coordinate.__universe.axes():
            secure = self._points[point]
            if secure < ref.map.lb:
                secure = ref.map.lb
            elif secure > ref.map.ub:
                secure = ref.map.ub
            self._points[point] = secure

    def lb(self, idx):
        _, ref = Coordinate.__universe.axes()[idx]
        return ref.map.lb

    def ub(self, idx):
        _, ref = Coordinate.__universe.axes()[idx]
        return ref.map.ub

    def euclideanDistance(self, other):
        diffs = sum([(x-y)**2 for x,y in zip(self._points, other._points)])
        return math.sqrt(diffs)

    def uniformRandom(self, idx=None):
        if idx is None:
            for point, ref in Coordinate.__universe.axes():
                self._points[point] = ref.map.uniformRandom()
        else:
           point, ref = Coordinate.__universe[idx]
           self._points[point] = ref.map.uniformRandom()

    def gaussianRandom(self, idx=None):
        if idx is None:
            for point, ref in Coordinate.__universe.axes():
                self._points[point] = ref.map.gaussianRandom()
        else:
           point, ref = Coordinate.__universe[idx]
           self._points[point] = ref.map.gaussianRandom()

    def cauchyRandom(self, idx=None):
        if idx is None:
            for point, ref in Coordinate.__universe.axes():
                self._points[point] = ref.map.cauchyRandom()
        else:
           point, ref = Coordinate.__universe[idx]
           self._points[point] = ref.map.cauchyRandom()

    def __add__(self, other):
        if isinstance(other, Coordinate):
            return list(map(add, self._points, other))
        elif isinstance(other, (int, float)):
            self._points[0] += other
            return copy.deepcopy(self._points)

    def __iadd__(self, other):
        c = Coordinate()
        c.set(list(map(add, self._points, other)))
        return c

    def __radd__(self, other):
        if other == 0:
            return self._points
        else:
            return list(map(lambda x: x+other, self._points))

    def __sub__(self, other):
        c = Coordinate()
        c.set(list(map(sub, self._points, other._points)))
        return c

    def __rsub__(self, other):
        c = Coordinate()
        c.set(list(map(sub, other._points, self._points)))
        return c

    def __mul__(self, other):
        raise NotImplementedError

    def __rmul__(self, other):
        c = Coordinate()
        if isinstance(other, (int, float)):
            c.set(list(map(lambda x: other*x, self._points)))
        else:
            raise NotImplementedError
        return c

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

    def __isub__(self, other):
        self._points = list(map(sub, self._points, other))

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

