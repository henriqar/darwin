"""
Date: 21/03/2020
"""
from types import MappingProxyType

class CoordinateModel(Model):
    """
    """
    _global_coordinateid = -1
    def __init__(self, coordinates=[]):
        CoordinateModel._global_coordinateid += 1
        self.coordinateid = CoordinateModel._global_coordinateid
        self.coordinates = coordinates

    def tojson(self):
        return {'coordinateid': self.coordinateid,
                'coordinates': self.coordinates}

