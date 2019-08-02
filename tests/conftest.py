
import pytest
import darwin
import numpy as np

@pytest.fixture
def supplyGeneticAlgorithm():
    opt = darwin.Algorithm(darwin.opt.GeneticAlgorithm)
    opt.mutationProbability = np.random.uniform(0.05, 0.25)
    opt.particles = np.random.randint(5, 20)
    opt.iterations = np.random.randint(5, 15)
    return opt

@pytest.fixture
def supplyBatAlgorithm():
    opt = darwin.Algorithm(darwin.opt.BatAlgorithm)
    opt.maxFrequency = np.random.uniform(0.3, 0.8)
    opt.minFrequency = np.random.uniform(0.2, 0.5)
    opt.pulseRate = np.random.uniform(0.3, 0.98)
    opt.loudness = np.random.uniform(0.5, 1.5)
    opt.particles = np.random.randint(5, 20)
    opt.iterations = np.random.randint(5, 15)
    return opt

@pytest.fixture
def supplyParticleSwarmOptimization():
    opt = darwin.Algorithm(darwin.opt.ParticleSwarmOptimization)
    opt.c1 = np.random.uniform(0, 1)
    opt.c2 = np.random.uniform(0, 1)
    opt.w = np.random.uniform(0, 1)
    opt.particles = np.random.randint(5, 20)
    opt.iterations = np.random.randint(5, 15)
    return opt

@pytest.fixture
def supplyFitnessFunction():
    def fitness():
        print(os.path.exists('output.txt'))
        with open('output.txt') as fp:
            return float(fp.read())
    return fitness
