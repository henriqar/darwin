
import darwin

def fitness():
    with open('output.txt') as fp:
        return float(fp.read())

# get the algorithm to gbe used for the op[timization
opt = darwin.Algorithm(darwin.opt.BatAlgorithm)

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

# exclusive required BA parameters
opt.max_frequency = 0.8
opt.min_frequency = 0.3
opt.pulse_rate = 0.9
opt.loudness = 1

opt.submitfile = 'sanity.submit'
opt.start()
