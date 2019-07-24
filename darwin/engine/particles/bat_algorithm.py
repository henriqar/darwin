
import logging

from .particle import Particle

logger = logging.getLogger(__name__)

class BatAlgorithm(Particle):
    def __init__(self):
        super().__init__()

        # augmented parameters
        self.frequency = 0 # .f frequency
        self.pulse_rate = 0 # .r pulse rate
        self.loudness = None # .A loudness

        # last position
        self.xl = None

