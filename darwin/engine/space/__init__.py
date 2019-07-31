
import copy

from .space import Space
from .coordinate import Coordinate

import darwin.engine.particles as particles

__all__ = ['Formatter', 'Coordinate', 'bigBang', 'dimension', 'expand',
        'addVariable', 'addExclusiveGroup', 'getOrigin']

class Formatter:
    """
    A Formatter class executes the convertion of the discrete variable.

    The Formatter class are passed as a parameter everytime a discrete variable
    is introduced in the solution space. The 'format' method from the Formatter
    object is used to convert the discrete variable as the user specified for
    the execution script.
    """
    def format(self, data):
        return str(data)

"""
Define the universe solution space for all particles generated in this
optimization.
"""
_universe = None

"""
Universe origin coordinate (0,0,0,...,0) reference for any dimension size
"""
_origin = None

def bigBang():
    """
    If the universe space is not allocated, we create the universe solution
    space, else return the same instance (singleton)
    """
    global _universe
    if _universe is None:
        _universe = Space()

def dimension():
    """
    Get the dimension of the solution space at the moment.
    """
    return _universe.dimension

def variable(idx):
    if _universe is None:
        logger.error('universe must be initialized with a bigBang')
        sys.exit(1)
    return _universe[idx]

def expand():
    """
    Expand function will expand the universe with all variables and groups
    given.

    The function will expand the universe to reach all variables and to
    prohibit every coordinate that is outside the users scope a.k.a
    define the group of coordinates that are valid for this optimization.
    """
    _universe.build()
    Coordinate.setUniverse(_universe)

    global _origin
    _origin = Coordinate()
    for particle in particles.particles():
        particle.position(_origin)

def getOrigin():
    """
    function to return the origin of the solution universe.
    """
    return copy.deepcopy(_origin)

def addVariable(name, mapping, formatter, discrete):
    """
    Adds a new variable axis for the solution space.

    :param name: A string indicating the name of the variable used.
    :param mapping: The map of variable values used for continuous or discrete
    values.
    :param formatter: Formatter object to format values, default is Formatter.
    :param discrete: indicate if the variable is continuous or discrete.
    """
    if isinstance(mapping, (tuple, list)):
        _universe.addParam(name, mapping, formatter, discrete)
    else:
        logger.error('mapping must be a iterable type')
        sys.exit(1)

def addExclusiveGroup(*groups):
    """
    Adds a new exclusive group of variables of the solution space.

    :param *groups: multiple tuple arguments defining mutual exclusive groups.
    """
    for group in groups:
        if not isinstance(group, (tuple, list)):
            logger.error('exclusive group must be a iterable type')
            sys.exit(1)
    else:
        _universe.addExclusiveGroup(*groups)

