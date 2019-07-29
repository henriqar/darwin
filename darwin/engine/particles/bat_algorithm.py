
import logging

from .particle import Particle

logger = logging.getLogger(__name__)

class BatAlgorithm(Particle):
    def __init__(self):
        super().__init__()
        self.frequency = 0
        self.pulse_rate = 0
        self.loudness = None
        self.last_coordinate = None

