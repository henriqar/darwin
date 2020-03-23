"""
Date: 21/03/2020
"""
import logging

logger = logging.getLogger(__name__)

class AnnealModel(ParticleModel):
    """
    """
    def __init__(self):
        super().__init__()

        # create anneal model for SimulatedAnnealing
        self.ub = 0
        self.lb = 0

