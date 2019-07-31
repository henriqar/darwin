
import logging

from .particle import Particle

logger = logging.getLogger(__name__)

class SimulatedAnnealing(Particle):
    def __init__(self):
        super().__init__()

        # augmented parameters
        self.UB = []
        self.LB = []


