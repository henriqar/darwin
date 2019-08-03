
import pytest
import darwin
import numpy as np

@pytest.fixture
def supplyBA():
    ba = darwin.Algorithm(darwin.opt.BatAlgorithm)
    ba.maxFrequency = np.random.uniform(0.3, 0.8)
    ba.minFrequency = np.random.uniform(0.2, 0.5)
    ba.pulseRate = np.random.uniform(0.3, 0.98)
    ba.loudness = np.random.uniform(0.5, 1.5)
    ba.particles = np.random.randint(5, 20)
    ba.iterations = np.random.randint(5, 15)
    return ba

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

# discrete used
map1 = (0, 1, 2, 3)
map2 = ('a', 'b', 'c', 'd')

def test_htcondor_ba(supplyBA, supplyFitnessFunction):
    supplyBA.executionEngine = darwin.drm.HTCondor
    supplyBA.addVariable('x', x)
    supplyBA.addVariable('y', y)
    supplyBA.function = supplyFitnessFunction
    supplyBA.submitFile = 'sanity.submit'
    supplyBA.start()

def test_htcondor_discrete_ba(supplyBA, supplyDiscreteFitnessFunction):
    supplyBA.executionEngine = darwin.drm.HTCondor
    supplyBA.addVariable('map1', map1, discrete=True)
    supplyBA.addVariable('map2', map2, discrete=True)
    supplyBA.function = supplyDiscreteFitnessFunction
    supplyBA.submitFile = 'sanity_discrete.submit'
    supplyBA.start()

def test_local_ba(supplyBA):
    supplyBA.executionEngine = darwin.drm.TaskSpooler
    supplyBA.addVariable('x', x)
    supplyBA.addVariable('y', y)
    supplyBA.function = supplyFitnessFunction
    supplyBA.submitFile = 'sanity.submit'
    supplyBA.start()

def test_local_discrete_ba(supplyBA, supplyDiscreteFitnessFunction):
    supplyBA.executionEngine = darwin.drm.TaskSpooler
    supplyBA.addVariable('map1', map1, discrete=True)
    supplyBA.addVariable('map2', map2, discrete=True)
    supplyBA.function = supplyDiscreteFitnessFunction
    supplyBA.submitFile = 'sanity_discrete.submit'
    supplyBA.start()
