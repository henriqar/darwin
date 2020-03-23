"""
"""
import tinydb
import logging

from .models import Models

logger = logging.getLogger(__name__)

class Database():
    """
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        """
        if cls._instance is None:
            return cls.__new__(*args, **kwargs)
        else:
            return cls._instance

    def __init__(self, optimization, name='darwin.json'):
        """
        """
        self.storage = TinyDB(name)
        self.optimization = optimization
        self.particles = self.storage.table('particles')
        self.iterations = self.storage.table('iterations')

    def create_particles(self, quantity, dimension):
        """
        """
        assert isinstance(quantity, int)
        assert isinstance(dimension, int)
        for i in quantity:
            particle = Models.particle_model(self.optimization)
            particle['id'] = i
            self.storage.insert(particle)


    def get_particle(self, index):
        """
        """
        assert isinstance(index, int)
        particle = tinyDB.Query()
        return self.particles.get(particle.id == index)
