
import darwin

fm = ((0, 1, 3), (1, 2), (6, 19), (2.1, 88))

def Quadratic():
    return 10

# get the algorithm to gbe used for the op[timization
opt = darwin.Algorithm(darwin.opt.GA)

# define the mapping parameters used
map1 = (1,2,3,4)
map2 = ('a', 'b', 'c', 'd')

opt.add_parameter('map1', map1, discrete=True)
opt.add_parameter('map2', map2, discrete=True)

# define htcondor execution engine
opt.exec_engine = darwin.drm.HTCONDOR

# default darwin parameters
opt.function = Quadratic
opt.agents = 10
opt.iterations = 10

# exclusive required GA parameters
opt.mutation_probability = 0.2

opt.submitfile = 'sanity.submit'
opt.start()
