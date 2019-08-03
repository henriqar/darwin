
import numpy as np
import darwin
import pytest

@pytest.fixture
def supplyPSO():
    pso = darwin.Algorithm(darwin.opt.ParticleSwarmOptimization)
    pso.c1 = np.random.uniform(0, 1)
    pso.c2 = np.random.uniform(0, 1)
    pso.w = np.random.uniform(0, 1)
    pso.particles = np.random.randint(5, 20)
    pso.iterations = np.random.randint(5, 15)
    return pso

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

# discrete used
map1 = (0,1,2,3)
map2 = ('a', 'b', 'c', 'd')

def test_htcondor_pso(supplyPSO, supplyFitnessFunction):
    supplyPSO.executionEngine = darwin.drm.HTCondor
    supplyPSO.addVariable('x', x)
    supplyPSO.addVariable('y', y)
    supplyPSO.function = supplyFitnessFunction
    supplyPSO.submitFile = 'sanity.submit'
    supplyPSO.start()

def test_htcondor_discrete_pso(supplyPSO, supplyDiscreteFitnessFunction):
    supplyPSO.executionEngine = darwin.drm.HTCondor
    supplyPSO.addVariable('map1', map1, discrete=True)
    supplyPSO.addVariable('map2', map2, discrete=True)
    supplyPSO.function = supplyDiscreteFitnessFunction
    supplyPSO.submitFile = 'sanity_discrete.submit'
    supplyPSO.start()

def test_local_pso(supplyPSO):
    supplyPSO.executionEngine = darwin.drm.TaskSpooler
    supplyPSO.addVariable('x', x)
    supplyPSO.addVariable('y', y)
    supplyPSO.function = supplyFitnessFunction
    supplyPSO.submitFile = 'sanity.submit'
    supplyPSO.start()

def test_local_discrete_pso(supplyPSO, supplyDiscreteFitnessFunction):
    supplyPSO.executionEngine = darwin.drm.TaskSpooler
    supplyPSO.addVariable('map1', map1, discrete=True)
    supplyPSO.addVariable('map2', map2, discrete=True)
    supplyPSO.function = supplyDiscreteFitnessFunction
    supplyPSO.submitFile = 'sanity_discrete.submit'
    supplyPSO.start()
