
import numpy as np
import darwin
import pytest

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

# discrete used
map1 = (0,1,2,3)
map2 = ('a', 'b', 'c', 'd')

def test_htcondor_pso(supplyFitnessFunction):
    pso = darwin.Algorithm(darwin.opt.ParticleSwarmOptimization)
    pso.c1 = np.random.uniform(0, 1)
    pso.c2 = np.random.uniform(0, 1)
    pso.w = np.random.uniform(0, 1)
    pso.particles = np.random.randint(5, 20)
    pso.iterations = np.random.randint(5, 15)
    pso.executionEngine = darwin.drm.HTCondor
    pso.addVariable('x', x)
    pso.addVariable('y', y)
    pso.function = supplyFitnessFunction
    pso.submitFile = 'sanity.submit'
    pso.start()

def test_htcondor_pso_discrete(supplyDiscreteFitnessFunction):
    pso = darwin.Algorithm(darwin.opt.ParticleSwarmOptimization)
    pso.c1 = np.random.uniform(0, 1)
    pso.c2 = np.random.uniform(0, 1)
    pso.w = np.random.uniform(0, 1)
    pso.particles = np.random.randint(5, 20)
    pso.iterations = np.random.randint(5, 15)
    pso.executionEngine = darwin.drm.HTCondor
    pso.addVariable('map1', map1, discrete=True)
    pso.addVariable('map2', map2, discrete=True)
    pso.function = supplyDiscreteFitnessFunction
    pso.submitFile = 'sanity_discrete.submit'
    pso.start()

def test_local_pso(supplyFitnessFunction):
    pso = darwin.Algorithm(darwin.opt.ParticleSwarmOptimization)
    pso.c1 = np.random.uniform(0, 1)
    pso.c2 = np.random.uniform(0, 1)
    pso.w = np.random.uniform(0, 1)
    pso.particles = np.random.randint(5, 20)
    pso.iterations = np.random.randint(5, 15)
    pso.executionEngine = darwin.drm.TaskSpooler
    pso.addVariable('x', x)
    pso.addVariable('y', y)
    pso.function = supplyFitnessFunction
    pso.submitFile = 'sanity.submit'
    pso.start()

def test_local_pso_discrete(supplyDiscreteFitnessFunction):
    pso = darwin.Algorithm(darwin.opt.ParticleSwarmOptimization)
    pso.c1 = np.random.uniform(0, 1)
    pso.c2 = np.random.uniform(0, 1)
    pso.w = np.random.uniform(0, 1)
    pso.particles = np.random.randint(5, 20)
    pso.iterations = np.random.randint(5, 15)
    pso.executionEngine = darwin.drm.TaskSpooler
    pso.addVariable('map1', map1, discrete=True)
    pso.addVariable('map2', map2, discrete=True)
    pso.function = supplyDiscreteFitnessFunction
    pso.submitFile = 'sanity_discrete.submit'
    pso.start()
