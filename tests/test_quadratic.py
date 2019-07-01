
import darwin

def Quadratic(map1=None, map2=None):
    print('map1: {}, map2: {}'.format(map1, map2))

    return 10

# get the algorithm to gbe used for the op[timization
opt = darwin.Algorithm(darwin.opt.GA)

# define the mapping parameters used
map1 = (1,2,3,4)
map2 = ('a', 'b', 'c', 'd')

opt.add_parameter(name='map1', param=map1, discrete=True)
opt.add_parameter(name='map2', param=map2, discrete=True)

opt.function = Quadratic
opt.agents = 10
opt.iterations = 10

# exclusive GA parameters
opt.mutation_probability = 0.2

opt.start()

