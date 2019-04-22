
import darwin

def Ackley_First(agent_list, *args):
    pass

# get the algorithm to gbe used for the op[timization
opt = darwin.algorithm('ga')

# define the mapping parameters used
map1 = (1,2,3,4)
map2 = ('a', 'b', 'c', 'd')

opt.add_parameter(map1)
opt.add_parameter(map2)
