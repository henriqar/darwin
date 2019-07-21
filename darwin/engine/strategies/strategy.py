
import abc
import logging

logger = logging.getLogger(__name__)

class Strategy():

    def __init__(self, data):
        self.data = data

    @abc.abstractmethod
    def initialize(self):
        raise NotImplementedError

    @abc.abstractmethod
    def fitness_evaluation(self):
        raise NotImplementedError

    @abc.abstractmethod
    def generator(self):
       raise NotImplementedError

