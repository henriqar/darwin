"""
Date: 21/03/2020
"""
import logging

logger = logging.getLogger(__name__)

class BirdModel(ParticleModel):
    """
    """
    def __init__(self):
        super().__init__()

        # create bird model for MigratingBirdsOptimization
        self.nb = 0

    def tojson(self):
        return super().tojson().update({'nb': self.nb})

