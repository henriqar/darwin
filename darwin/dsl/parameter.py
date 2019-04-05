
import itertools
import copy

class parameter:

    def __init__(self, iterable):

        if isinstance(iterable, tuple):
            # force iterable to be tuple, not modifyable
            self.iterable = set(iterable)
        else:
            raise TypeError("map iterable must be a tuple type")

    def __add__(self, other):
        return Map(tuple(self.iterable) + tuple(other.iterable))

    def __iadd__(self, other):
        return Map(self.iterable + (other,))

    def __radd__(self, other):
        return Map(other.iterable + self.iterable)

    def __sub__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __mul__(self, other):
        return Map(tuple(itertools.product(self.iterable, other.iterable)))

    def __imul__(self, other):
        return Map(tuple(itertools.product(self.iterable, (other,))))

    def __rmul__(self, other):
        return Map(tuple(itertools.product(other.iterable, self.iterable)))

    def __div__(self, other):
        pass

    def __idiv__(self, other):
        pass

    def __rdiv__(self, other):
        pass

