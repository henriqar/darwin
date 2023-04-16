
import pytest
import darwin
import numpy as np

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

# discrete used
map1 = (0, 1, 2, 3)
map2 = ('a', 'b', 'c', 'd')

def test_htcondor_ba_continuous(supplyFitnessFunction):
    ba = darwin.Algorithm(darwin.opt.BatAlgorithm)
    ba.maxFrequency = np.random.uniform(0.3, 0.8)
    ba.minFrequency = np.random.uniform(0.2, 0.5)
    ba.pulseRate = np.random.uniform(0.3, 0.98)
    ba.loudness = np.random.uniform(0.5, 1.5)
    ba.particles = np.random.randint(5, 20)
    ba.iterations = np.random.randint(5, 15)
    ba.executionEngine = darwin.drm.HTCondor
    ba.addVariable('x', x)
    ba.addVariable('y', y)
    ba.function = supplyFitnessFunction
    ba.submitFile = 'sanity.submit'
    ba.start()

def test_htcondor_ba_continuous_autosubmit(supplyFitnessFunction):
    ba = darwin.Algorithm(darwin.opt.BatAlgorithm)
    ba.maxFrequency = np.random.uniform(0.3, 0.8)
    ba.minFrequency = np.random.uniform(0.2, 0.5)
    ba.pulseRate = np.random.uniform(0.3, 0.98)
    ba.loudness = np.random.uniform(0.5, 1.5)
    ba.particles = np.random.randint(5, 20)
    ba.iterations = np.random.randint(5, 15)
    ba.executionEngine = darwin.drm.HTCondor
    ba.addVariable('x', x)
    ba.addVariable('y', y)
    ba.function = supplyFitnessFunction
    ba.autoSubmitFile = darwin.auto.SubmitFile
    ba.start()

def test_htcondor_ba_discrete(supplyDiscreteFitnessFunction):
    ba = darwin.Algorithm(darwin.opt.BatAlgorithm)
    ba.maxFrequency = np.random.uniform(0.3, 0.8)
    ba.minFrequency = np.random.uniform(0.2, 0.5)
    ba.pulseRate = np.random.uniform(0.3, 0.98)
    ba.loudness = np.random.uniform(0.5, 1.5)
    ba.particles = np.random.randint(5, 20)
    ba.iterations = np.random.randint(5, 15)
    ba.executionEngine = darwin.drm.HTCondor
    ba.addVariable('map1', map1, discrete=True)
    ba.addVariable('map2', map2, discrete=True)
    ba.function = supplyDiscreteFitnessFunction
    ba.submitFile = 'sanity_discrete.submit'
    ba.start()

def test_local_ba_continuous(supplyFitnessFunction):
    ba = darwin.Algorithm(darwin.opt.BatAlgorithm)
    ba.maxFrequency = np.random.uniform(0.3, 0.8)
    ba.minFrequency = np.random.uniform(0.2, 0.5)
    ba.pulseRate = np.random.uniform(0.3, 0.98)
    ba.loudness = np.random.uniform(0.5, 1.5)
    ba.particles = np.random.randint(5, 20)
    ba.iterations = np.random.randint(5, 15)
    ba.executionEngine = darwin.drm.TaskSpooler
    ba.addVariable('x', x)
    ba.addVariable('y', y)
    ba.function = supplyFitnessFunction
    ba.submitFile = 'sanity.submit'
    ba.start()

def test_local_ba_discrete(supplyDiscreteFitnessFunction):
    ba = darwin.Algorithm(darwin.opt.BatAlgorithm)
    ba.maxFrequency = np.random.uniform(0.3, 0.8)
    ba.minFrequency = np.random.uniform(0.2, 0.5)
    ba.pulseRate = np.random.uniform(0.3, 0.98)
    ba.loudness = np.random.uniform(0.5, 1.5)
    ba.particles = np.random.randint(5, 20)
    ba.iterations = np.random.randint(5, 15)
    ba.executionEngine = darwin.drm.TaskSpooler
    ba.addVariable('map1', map1, discrete=True)
    ba.addVariable('map2', map2, discrete=True)
    ba.function = supplyDiscreteFitnessFunction
    ba.submitFile = 'sanity_discrete.submit'
    ba.start()
