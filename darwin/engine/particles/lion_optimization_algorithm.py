
import logging

from .particle import Particle

logger = loggin.getLogger(__name__)

class LionOptimizationAlgorithm:
    def __init__(self):
        super().__init__()

        # augmented parameters
        self.xl = None
        self.prev_x = None
        self.bestfit = sys.maxsize
        self.previousfit = sys.maxsize

