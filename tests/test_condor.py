
import darwin

def Quadratic(map1=None, map2=None):
    print('map1: {}'.format(map1))
    print('map2: {}'.format(map2))

    return 10

# get the algorithm to gbe used for the op[timization
opt = darwin.algorithm('ga')

# set cluster usage
opt.set_exec_engine(engine=darwin.constants.HTCONDOR)

map1 = (1,2,3,4)
map2 = ('a', 'b', 'c', 'd')

opt.add_parameter(name='map1', param=map1)
opt.add_parameter(name='map2', param=map2)

opt.set_function(Quadratic)
opt.set_agents(10)
opt.set_max_iterations(3)

# exclusive GA parameters
opt.set_mutation_probability(0.2)

opt.start()

