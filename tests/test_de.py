
import pytest
import darwin
import numpy as np

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

# discrete used
map1 = (0, 1, 2, 3)
map2 = ('a', 'b', 'c', 'd')

def test_htcondor_de_continuous(supplyFitnessFunction):
    de = darwin.Algorithm(darwin.opt.DifferentialEvolution)
    de.mutationFactor = np.random.uniform(0.05, 0.25)
    de.crossoverProbability = np.random.uniform(0.05, 0.25)
    de.particles = np.random.randint(5, 15)
    de.iterations = np.random.randint(5, 15)
    de.executionEngine = darwin.drm.HTCondor
    de.addVariable('x', x)
    de.addVariable('y', y)
    de.function = supplyFitnessFunction
    de.submitFile = 'sanity.submit'
    de.start()

def test_htcondor_de_discrete(supplyDiscreteFitnessFunction):
    de = darwin.Algorithm(darwin.opt.DifferentialEvolution)
    de.mutationFactor = np.random.uniform(0.05, 0.25)
    de.crossoverProbability = np.random.uniform(0.05, 0.25)
    de.particles = np.random.randint(5, 15)
    de.iterations = np.random.randint(5, 15)
    de.executionEngine = darwin.drm.HTCondor
    de.addVariable('map1', map1, discrete=True)
    de.addVariable('map2', map2, discrete=True)
    de.function = supplyDiscreteFitnessFunction
    de.submitFile = 'sanity_discrete.submit'
    de.start()

def test_local_de_continuous(supplyFitnessFunction):
    de = darwin.Algorithm(darwin.opt.DifferentialEvolution)
    de.mutationFactor = np.random.uniform(0.05, 0.25)
    de.crossoverProbability = np.random.uniform(0.05, 0.25)
    de.particles = np.random.randint(5, 15)
    de.iterations = np.random.randint(5, 15)
    de.executionEngine = darwin.drm.TaskSpooler
    de.addVariable('x', x)
    de.addVariable('y', y)
    de.function = supplyFitnessFunction
    de.submitFile = 'sanity.submit'
    de.start()

def test_local_de_discrete(supplyDiscreteFitnessFunction):
    de = darwin.Algorithm(darwin.opt.DifferentialEvolution)
    de.mutationFactor = np.random.uniform(0.05, 0.25)
    de.crossoverProbability = np.random.uniform(0.05, 0.25)
    de.particles = np.random.randint(5, 15)
    de.iterations = np.random.randint(5, 15)
    de.executionEngine = darwin.drm.TaskSpooler
    de.addVariable('map1', map1, discrete=True)
    de.addVariable('map2', map2, discrete=True)
    de.function = supplyDiscreteFitnessFunction
    de.submitFile = 'sanity_discrete.submit'
    de.start()
