
import numpy as np
import darwin
import pytest

@pytest.fixture
def supplySA():
    sa = darwin.Algorithm(darwin.opt.SimulatedAnnealing)
    sa.initialTemperature = np.random.uniform(0, 1)
    sa.finalTemperature = np.random.uniform(1.5, 3.5)
    sa.particles = np.random.randint(5, 20)
    sa.iterations = np.random.randint(5, 15)
    return sa

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

# discrete used
map1 = (0,1,2,3)
map2 = ('a', 'b', 'c', 'd')

def test_htcondor_sa(supplySA, supplyFitnessFunction):
    supplySA.executionEngine = darwin.drm.HTCondor
    supplySA.addVariable('x', x)
    supplySA.addVariable('y', y)
    supplySA.function = supplyFitnessFunction
    supplySA.submitFile = 'sanity.submit'
    supplySA.start()

def test_htcondor_discrete_sa(supplySA, supplyDiscreteFitnessFunction):
    supplySA.executionEngine = darwin.drm.HTCondor
    supplySA.addVariable('map1', map1, discrete=True)
    supplySA.addVariable('map2', map2, discrete=True)
    supplySA.function = supplyDiscreteFitnessFunction
    supplySA.submitFile = 'sanity_discrete.submit'
    supplySA.start()

def test_local_sa(supplySA):
    supplySA.executionEngine = darwin.drm.TaskSpooler
    supplySA.addVariable('x', x)
    supplySA.addVariable('y', y)
    supplySA.function = supplyFitnessFunction
    supplySA.submitFile = 'sanity.submit'
    supplySA.start()

def test_local_discrete_sa(supplySA, supplyDiscreteFitnessFunction):
    supplySA.executionEngine = darwin.drm.TaskSpooler
    supplySA.addVariable('map1', map1, discrete=True)
    supplySA.addVariable('map2', map2, discrete=True)
    supplySA.function = supplyDiscreteFitnessFunction
    supplySA.submitFile = 'sanity_discrete.submit'
    supplySA.start()
