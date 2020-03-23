"""
Date: 21/03/2020
"""
import logging

logger = logging.getLogger(__name__)

class SwarmModel(ParticleModel):
    """
    """
    def __init__(self):
        super().__init__()

        # create swarm model for ParticleSwarmOptimization
        self.v = 0
        self.xl = []
        self.pfit = []
        self.t_v = []
        self.t_xl = []

    def tojson(self):
        local = {'v': self.v, 'xl': self.xl, 'pfit': self.pfit,
                 't_v': self.t_v, 't_xl': self.t_xl}
        return super().tojson().update(local)

