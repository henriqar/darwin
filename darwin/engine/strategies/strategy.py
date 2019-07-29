
import abc
import logging

from darwin.engine.particles import getBestFitness

from itertools import chain

logger = logging.getLogger(__name__)

class Strategy():

    def __init__(self, data):
        self.data = data

    @abc.abstractmethod
    def initialize(self):
        raise NotImplementedError

    @abc.abstractmethod
    def fitnessEvaluation(self):
        raise NotImplementedError

    @abc.abstractmethod
    def algorithm(self):
        raise NotImplementedError

    def iterations(self):
        """
        """
        for v in chain(self.initialize(), self.algorithm()):
            yield v

        print('\nFINISHED - OK (minimum fitness value {})'.format(
            getBestFitness()))


