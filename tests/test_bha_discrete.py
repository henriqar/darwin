
import darwin

fm = {
    'a': (10, 20, 1000, 1.2),
    'b': (0.001, 3, 88, 76),
    'c': (99, 34, 3.2, 1.0),
    'd': (9.4, 773.2, 1098.56, 0.5)
}

def fitness():
    with open('output.txt') as fp:
        line = fp.readline()
        line = list(filter(None, line.strip().split('-map2')))
        letter = line[1].strip()
        line = list(filter(None, line[0].strip().split('-map1')))
        number = int(line[0].strip())

        return fm[letter][number]

# get the algorithm to gbe used for the op[timization
opt = darwin.Algorithm(darwin.opt.BlackHoleAlgorithm)

# define the mapping parameters used
map1 = (0,1,2,3)
map2 = ('a', 'b', 'c', 'd')

opt.addVariable('map1', map1, discrete=True)
opt.addVariable('map2', map2, discrete=True)

# define htcondor execution engine
opt.executionEngine = darwin.drm.HTCondor

# default darwin parameters
opt.function = fitness
opt.particles = 10
opt.iterations = 10

opt.submitFile = 'sanity_discrete.submit'
opt.start()
