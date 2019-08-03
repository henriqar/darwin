
import pytest
import darwin
import numpy as np

@pytest.fixture
def supplyBHA():
    bha = darwin.Algorithm(darwin.opt.BlackHoleAlgorithm)
    bha.particles = np.random.randint(5, 20)
    bha.iterations = np.random.randint(5, 15)
    return bha

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

# discrete used
map1 = (0,1,2,3)
map2 = ('a', 'b', 'c', 'd')

def test_htcondor_bha(supplyBHA, supplyFitnessFunction):
    supplyBHA.executionEngine = darwin.drm.HTCondor
    supplyBHA.addVariable('x', x)
    supplyBHA.addVariable('y', y)
    supplyBHA.function = supplyFitnessFunction
    supplyBHA.submitFile = 'sanity.submit'
    supplyBHA.start()

def test_htcondor_discrete_bha(supplyBHA, supplyDiscreteFitnessFunction):
    supplyBHA.executionEngine = darwin.drm.HTCondor
    supplyBHA.addVariable('map1', map1, discrete=True)
    supplyBHA.addVariable('map2', map2, discrete=True)
    supplyBHA.function = supplyDiscreteFitnessFunction
    supplyBHA.submitFile = 'sanity_discrete.submit'
    supplyBHA.start()

def test_local_bha(supplyBHA):
    supplyBHA.executionEngine = darwin.drm.TaskSpooler
    supplyBHA.addVariable('x', x)
    supplyBHA.addVariable('y', y)
    supplyBHA.function = supplyFitnessFunction
    supplyBHA.submitFile = 'sanity.submit'
    supplyBHA.start()

def test_local_discrete_bha(supplyBHA, supplyDiscreteFitnessFunction):
    supplyBHA.executionEngine = darwin.drm.TaskSpooler
    supplyBHA.addVariable('map1', map1, discrete=True)
    supplyBHA.addVariable('map2', map2, discrete=True)
    supplyBHA.function = supplyDiscreteFitnessFunction
    supplyBHA.submitFile = 'sanity_discrete.submit'
    supplyBHA.start()


