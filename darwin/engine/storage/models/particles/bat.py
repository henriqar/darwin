"""
Date: 21/03/2020
"""
import logging

logger = logging.getLogger(__name__)

class BatModel(ParticleModel):
    """
    """
    def __init__(self, iteration):
        super().__init__(iteration)

        # create bat model for BatAlgorithm
        self.frequency = 0
        self.pulse_rate = 0
        self.loudness = 0
        self.last_coordinate = []

    def tojson(self):
        local = {'frequency': self.frequency, 'pulse_rate': self.pulse_rate,
                 'loudness': self.loudness,
                 'last_coordinate': self.last_coordinate}
        return super().tojson().update(local)


