
import darwin

def fitness():
    with open('output.txt') as fp:
        return float(fp.read())

# get the algorithm to gbe used for the op[timization
opt = darwin.Algorithm(darwin.opt.GeneticAlgorithm)

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

opt.add_parameter('x', x)
opt.add_parameter('y', y)

# define htcondor execution engine
opt.exec_engine = darwin.drm.HTCondor

# default darwin parameters
opt.function = fitness
opt.particles = 10
opt.iterations = 10

# exclusive required GA parameters
opt.mutation_probability = 0.05

opt.submitfile = 'sanity.submit'
opt.start()
