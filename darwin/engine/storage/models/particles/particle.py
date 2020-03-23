"""
Date: 21/03/2020
"""
import logging
import sys

logger = logging.getLogger(__name__)

class ParticleModel(Model):
    """
    """
    _global_particleid = -1
    def __init__(self, iteration_id = -1):
        ParticleModel._global_particleid += 1
        self.particleid = ParticleModel._global_particleid
        self.iterationid = iteration_id
        self.fitness = sys.maxsize
        self.coordinateid = -1

    def tojson(self):
        return {'particleid', self.particleid, 'iterationid': self.iterationd,
                'fitness': self.fitness, 'coordinateid': self.coordinateid}
