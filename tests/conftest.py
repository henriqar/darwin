
import pytest
import darwin
import numpy as np


fm = {
    'a': (10, 20, 1000, 1.2),
    'b': (0.001, 3, 88, 76),
    'c': (99, 34, 3.2, 1.0),
    'd': (9.4, 773.2, 1098.56, 0.5)
}

@pytest.fixture
def supplyFitnessFunction():
    def fitness():
        with open('output.txt') as fp:
            return float(fp.read())
    return fitness

@pytest.fixture
def supplyDiscreteFitnessFunction():
    def fitness():
        with open('output.txt') as fp:
            number = int(fp.readline().strip())
            letter = fp.readline().strip()
            return fm[letter][number]
    return fitness
