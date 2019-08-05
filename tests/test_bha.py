
import pytest
import darwin
import numpy as np

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

# discrete used
map1 = (0,1,2,3)
map2 = ('a', 'b', 'c', 'd')

def test_htcondor_bha_continuous(supplyFitnessFunction):
    bha = darwin.Algorithm(darwin.opt.BlackHoleAlgorithm)
    bha.particles = np.random.randint(5, 20)
    bha.iterations = np.random.randint(5, 15)
    bha.executionEngine = darwin.drm.HTCondor
    bha.addVariable('x', x)
    bha.addVariable('y', y)
    bha.function = supplyFitnessFunction
    bha.submitFile = 'sanity.submit'
    bha.start()

def test_htcondor_bha_discrete(supplyDiscreteFitnessFunction):
    bha = darwin.Algorithm(darwin.opt.BlackHoleAlgorithm)
    bha.particles = np.random.randint(5, 20)
    bha.iterations = np.random.randint(5, 15)
    bha.executionEngine = darwin.drm.HTCondor
    bha.addVariable('map1', map1, discrete=True)
    bha.addVariable('map2', map2, discrete=True)
    bha.function = supplyDiscreteFitnessFunction
    bha.submitFile = 'sanity_discrete.submit'
    bha.start()

def test_local_bha_continuous(supplyFitnessFunction):
    bha = darwin.Algorithm(darwin.opt.BlackHoleAlgorithm)
    bha.particles = np.random.randint(5, 20)
    bha.iterations = np.random.randint(5, 15)
    bha.executionEngine = darwin.drm.TaskSpooler
    bha.addVariable('x', x)
    bha.addVariable('y', y)
    bha.function = supplyFitnessFunction
    bha.submitFile = 'sanity.submit'
    bha.start()

def test_local_bha_discrete(supplyDiscreteFitnessFunction):
    bha = darwin.Algorithm(darwin.opt.BlackHoleAlgorithm)
    bha.particles = np.random.randint(5, 20)
    bha.iterations = np.random.randint(5, 15)
    bha.executionEngine = darwin.drm.TaskSpooler
    bha.addVariable('map1', map1, discrete=True)
    bha.addVariable('map2', map2, discrete=True)
    bha.function = supplyDiscreteFitnessFunction
    bha.submitFile = 'sanity_discrete.submit'
    bha.start()


