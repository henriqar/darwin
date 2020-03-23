"""
Date: 21/03/2020
"""
import logging
import sys

logger = logging.getLogger(__name__)

class IterationModel(Model):
    """
    """
    _global_iterationid = -1
    def __init__(self):
        IterationModel._iter_id += 1
        self.iterationid = IterationModel._global_iterationid
        self.best_fitness = sys.maxsize
        self.best_particleid = -1

    def tojson(self):
        return {'iterationid': self.iterationid,
                'best_fitness': self.best_fitness,
                'best_particleid': self.best_particleid}
