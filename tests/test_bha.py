
import darwin

def fitness():
    try:
        with open('output.txt') as fp:
            return float(fp.read())
    except:
        import pdb; pdb.set_trace()

# get the algorithm to gbe used for the op[timization
opt = darwin.Algorithm(darwin.opt.BlackHoleAlgorithm)

# define the mapping parameters used
x = (-200,+200)
y = (-1000,+1000)

opt.addVariable('x', x)
opt.addVariable('y', y)

# define htcondor execution engine
opt.executionEngine = darwin.drm.HTCondor

# default darwin parameters
opt.function = fitness
opt.particles = 10
opt.iterations = 10

opt.submitFile = 'sanity.submit'
opt.start()
