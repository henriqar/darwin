
import pytest
import darwin
import numpy as np

@pytest.fixture
def supplyGA():
    ga = darwin.Algorithm(darwin.opt.GeneticAlgorithm)
    ga.mutationProbability = np.random.uniform(0.05, 0.25)
    ga.particles = np.random.randint(5, 20)
    ga.iterations = np.random.randint(5, 15)
    return ga

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

# discrete used
map1 = (0,1,2,3)
map2 = ('a', 'b', 'c', 'd')

def test_htcondor_ga(supplyGA, supplyFitnessFunction):
    supplyGA.executionEngine = darwin.drm.HTCondor
    supplyGA.addVariable('x', x)
    supplyGA.addVariable('y', y)
    supplyGA.function = supplyFitnessFunction
    supplyGA.submitFile = 'sanity.submit'
    supplyGA.start()

def test_htcondor_discrete_ga(supplyGA, supplyDiscreteFitnessFunction):
    supplyGA.executionEngine = darwin.drm.HTCondor
    supplyGA.addVariable('map1', map1, discrete=True)
    supplyGA.addVariable('map2', map2, discrete=True)
    supplyGA.function = supplyDiscreteFitnessFunction
    supplyGA.submitFile = 'sanity_discrete.submit'
    supplyGA.start()

def test_local_ga(supplyGA):
    supplyGA.executionEngine = darwin.drm.TaskSpooler
    supplyGA.addVariable('x', x)
    supplyGA.addVariable('y', y)
    supplyGA.function = supplyFitnessFunction
    supplyGA.submitFile = 'sanity.submit'
    supplyGA.start()

def test_local_discrete_ga(supplyGA, supplyDiscreteFitnessFunction):
    supplyGA.executionEngine = darwin.drm.TaskSpooler
    supplyGA.addVariable('map1', map1, discrete=True)
    supplyGA.addVariable('map2', map2, discrete=True)
    supplyGA.function = supplyDiscreteFitnessFunction
    supplyGA.submitFile = 'sanity_discrete.submit'
    supplyGA.start()
