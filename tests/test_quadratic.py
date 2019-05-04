
import darwin

def Quadratic(map1=None, map2=None):
    print('map1: {}'.format(map1))
    print('map2: {}'.format(map2))

# get the algorithm to gbe used for the op[timization
opt = darwin.algorithm('ga')

# define the mapping parameters used
map1 = (1,2,3,4)
map2 = ('a', 'b', 'c', 'd')

opt.add_parameter(name='map1', param=map1)
opt.add_parameter(name='map2', param=map2)

opt.set_function(Quadratic)
opt.set_agents(10)
opt.set_max_iterations(10)

opt.start()

