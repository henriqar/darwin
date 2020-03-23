"""
Date: 21/03/2020
"""
import logging

logger = logging.getLogger(__name__)

class LionModel(ParticleModel):
    """
    """
    def __init__(self):
        super().__init__()

        # create lion for LionOptimizationAlgorithm
        self.xl = []
        self.prev_x = []
        self.bestfit = 0
        self.previous_fit = []

    def tojson(self):
        local = {'xl': self.xl, 'prev_x': self.prev_x, 'bestfit': self.bestfit,
                 'previous_fit': self.previous_fit}
        return super().tojson().update(local)


