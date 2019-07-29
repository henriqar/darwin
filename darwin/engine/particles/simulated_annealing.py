
import logging

from .particle import Particle

logger = logging.getLogger(__name__)

class SimulatedAnnealing(Particle):
    def __init__(self):
        super().__init__()

        # augmented parameters
        UB = 0
        LB = 0


