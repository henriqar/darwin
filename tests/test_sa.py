
import numpy as np
import darwin
import pytest

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

# discrete used
map1 = (0,1,2,3)
map2 = ('a', 'b', 'c', 'd')

def test_htcondor_sa(supplyFitnessFunction):
    sa = darwin.Algorithm(darwin.opt.SimulatedAnnealing)
    sa.initialTemperature = np.random.uniform(0, 1)
    sa.finalTemperature = np.random.uniform(1.5, 3.5)
    sa.particles = np.random.randint(5, 20)
    sa.iterations = np.random.randint(5, 15)
    sa.executionEngine = darwin.drm.HTCondor
    sa.addVariable('x', x)
    sa.addVariable('y', y)
    sa.function = supplyFitnessFunction
    sa.submitFile = 'sanity.submit'
    sa.start()

def test_htcondor_sa_discrete(supplyDiscreteFitnessFunction):
    sa = darwin.Algorithm(darwin.opt.SimulatedAnnealing)
    sa.initialTemperature = np.random.uniform(0, 1)
    sa.finalTemperature = np.random.uniform(1.5, 3.5)
    sa.particles = np.random.randint(5, 20)
    sa.iterations = np.random.randint(5, 15)
    sa.executionEngine = darwin.drm.HTCondor
    sa.addVariable('map1', map1, discrete=True)
    sa.addVariable('map2', map2, discrete=True)
    sa.function = supplyDiscreteFitnessFunction
    sa.submitFile = 'sanity_discrete.submit'
    sa.start()

def test_local_sa(supplyFitnessFunction):
    sa = darwin.Algorithm(darwin.opt.SimulatedAnnealing)
    sa.initialTemperature = np.random.uniform(0, 1)
    sa.finalTemperature = np.random.uniform(1.5, 3.5)
    sa.particles = np.random.randint(5, 20)
    sa.iterations = np.random.randint(5, 15)
    sa.executionEngine = darwin.drm.TaskSpooler
    sa.addVariable('x', x)
    sa.addVariable('y', y)
    sa.function = supplyFitnessFunction
    sa.submitFile = 'sanity.submit'
    sa.start()

def test_local_sa_discrete(supplyDiscreteFitnessFunction):
    sa = darwin.Algorithm(darwin.opt.SimulatedAnnealing)
    sa.initialTemperature = np.random.uniform(0, 1)
    sa.finalTemperature = np.random.uniform(1.5, 3.5)
    sa.particles = np.random.randint(5, 20)
    sa.iterations = np.random.randint(5, 15)
    sa.executionEngine = darwin.drm.TaskSpooler
    sa.addVariable('map1', map1, discrete=True)
    sa.addVariable('map2', map2, discrete=True)
    sa.function = supplyDiscreteFitnessFunction
    sa.submitFile = 'sanity_discrete.submit'
    sa.start()
