
import pytest
import darwin
import numpy as np

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

# discrete used
map1 = (0,1,2,3)
map2 = ('a', 'b', 'c', 'd')

def test_htcondor_ga_continuous(supplyFitnessFunction):
    ga = darwin.Algorithm(darwin.opt.GeneticAlgorithm)
    ga.mutationProbability = np.random.uniform(0.05, 0.25)
    ga.particles = np.random.randint(5, 15)
    ga.iterations = np.random.randint(5, 15)
    ga.executionEngine = darwin.drm.HTCondor
    ga.addVariable('x', x)
    ga.addVariable('y', y)
    ga.function = supplyFitnessFunction
    ga.submitFile = 'sanity.submit'
    ga.start()

def test_htcondor_ga_discrete(supplyDiscreteFitnessFunction):
    ga = darwin.Algorithm(darwin.opt.GeneticAlgorithm)
    ga.mutationProbability = np.random.uniform(0.05, 0.25)
    ga.particles = np.random.randint(5, 15)
    ga.iterations = np.random.randint(5, 15)
    ga.executionEngine = darwin.drm.HTCondor
    ga.addVariable('map1', map1, discrete=True)
    ga.addVariable('map2', map2, discrete=True)
    ga.function = supplyDiscreteFitnessFunction
    ga.submitFile = 'sanity_discrete.submit'
    ga.start()

def test_local_ga_continuous(supplyFitnessFunction):
    ga = darwin.Algorithm(darwin.opt.GeneticAlgorithm)
    ga.mutationProbability = np.random.uniform(0.05, 0.25)
    ga.particles = np.random.randint(5, 15)
    ga.iterations = np.random.randint(5, 15)
    ga.executionEngine = darwin.drm.TaskSpooler
    ga.addVariable('x', x)
    ga.addVariable('y', y)
    ga.function = supplyFitnessFunction
    ga.submitFile = 'sanity.submit'
    ga.start()

def test_local_ga_discrete(supplyDiscreteFitnessFunction):
    ga = darwin.Algorithm(darwin.opt.GeneticAlgorithm)
    ga.mutationProbability = np.random.uniform(0.05, 0.25)
    ga.particles = np.random.randint(5, 15)
    ga.iterations = np.random.randint(5, 15)
    ga.executionEngine = darwin.drm.TaskSpooler
    ga.addVariable('map1', map1, discrete=True)
    ga.addVariable('map2', map2, discrete=True)
    ga.function = supplyDiscreteFitnessFunction
    ga.submitFile = 'sanity_discrete.submit'
    ga.start()
