
import logging

from .particle import Particle

logger = getLogger(__name__)

class MigratingBirdsOptimization(Particle):
    def __init__(self):
        super().__init__()

        # augmented parameters
        self.nb = None

