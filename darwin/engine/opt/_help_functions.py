
import numpy as np

def gen_discrete_random_umber(low, high):

    random_nums = np.random.normal(scale=3, size=100000)
    random_ints = np.round(random_nums)

    return random_ints

def gen_gaussian_random_number(mean, variance):
    pass

def gen_cauchy_random_number(location, scale):
    pass

def gen_levy_distribution(n, beta):
    pass

def euclidean_distance(double *x, double *y, int n):
    pass

def GetPerpendicularVector(double *x, int n):
    pass

def NormalizeVector(double *x, int n):
    pass

def SortAgent(const void *a, const void *b):
    pass

def SortDataByVal(const void *a, const void *b):
    pass

def WaiveComment(FILE *fp):
    pass

def ReadSearchSpaceFromFile(char *fileName, int opt_id):
    pass

def getFUNCTIONid(char *s):
    pass

def RouletteSelection(SearchSpace *s, int k):
    pass

# def RouletteSelectionGA(population):
#     max = sum([c.fit for c in population.a])
#     selection_probs = [c.fit/max for c in population.a]
#     return population.a[np.random.choice(len(population.a), p=selection_probs)]
