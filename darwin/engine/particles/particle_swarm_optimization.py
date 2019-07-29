
import logging

from .particle import Particle

logger = logging.getLogger(__name__)

class ParticleSwarmOptimization(Particle):
    def __init__(self):
        super().__init__()

        # augmented parameters
        self.v = None
        self.xl = None

        # AIWPSO
        self.pfit = 0.0 # fitness value of the previous iteration

        # TensorPSO
        self.t_v = [] # tensor velocity (matrix)
        self.t_xl = [] # tensor local best (matrix)


