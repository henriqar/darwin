
import abc
import logging

logger = logging.getLogger(__name__)

class Strategy():

    def __init__(self, data):
        self.data = data

    @abc.abstractmethod
    def initialize(self, particles):
        raise NotImplementedError

    @abc.abstractmethod
    def generator(self, particles):
       raise NotImplementedError

