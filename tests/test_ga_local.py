
import os
import darwin

def fitness():
    with open('output.txt') as fp:
        return float(fp.read())

# get the algorithm to gbe used for the op[timization
opt = darwin.Algorithm(darwin.opt.GeneticAlgorithm)

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

opt.addVariable('x', x)
opt.addVariable('y', y)

# define htcondor execution engine
opt.executionEngine = darwin.drm.TaskSpooler

# default darwin parameters
opt.function = fitness
opt.particles = 10
opt.iterations = 10
opt.parallelJobs = 2

# exclusive required GA parameters
opt.mutationProbability = 0.05

opt.submitFile = 'sanity.submit'
opt.start()
