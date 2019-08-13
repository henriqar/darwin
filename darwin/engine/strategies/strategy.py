
import abc
import logging
import copy

# from darwin.engine.particles import getBestFitness, getBestCoordinate
import darwin.engine.space as universe
import darwin.engine.particles as particles

from itertools import chain

logger = logging.getLogger(__name__)

class Strategy():

    def __init__(self, data):
        self.data = data

    @abc.abstractmethod
    def initialize(self):
        raise NotImplementedError

    @abc.abstractmethod
    def evaluation(self):
        raise NotImplementedError

    @abc.abstractmethod
    def algorithm(self):
        raise NotImplementedError

    def cleanUp(self):
        pass

    def _innerGlobalEvaluation(self, gfit, gcoord):
        if gcoord is None:
            gcoord = universe.getOrigin()

        particle = min(particles.particles(), key=lambda x: x.fitness)
        if particle.fitness < gfit:
            return (particle.fitness, particle.copyCoord())
        return (gfit, gcoord)

    def globalEvaluation(self, gfit, gcoord):
        if gcoord is None:
            gcoord = universe.getOrigin()

        glob = self._innerGlobalEvaluation(gfit, gcoord)
        if glob is None:
            return (gfit, gcoord)
        else:
            return glob

    def iterations(self):
        """
        """
        for v in chain(self.initialize(), self.algorithm()):
            yield v

        print('\nFINISHED - OK (minimum fitness value {})'.format(
            particles.getBestFitness()))
        print('\nBest universe coordinate found:\n\n{0!s}\n'.format(
            particles.getBestCoordinate()))
        logger.info('\nBest universe coordinate found:\n\n{0!r}\n'.format(
            particles.getBestCoordinate()))


