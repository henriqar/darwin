
import collections
import logging
import sys
import contextlib
import os
import copy


logger = logging.getLogger(__name__)

class Particle():

    _instance_count = 0

    def __init__(self):
        self.coordinate = None
        self.intermediate = sys.maxsize
        self.fitness = sys.maxsize
        self.name = 'particle_{}'.format(Particle._instance_count)
        Particle._instance_count += 1

    def __setitem__(self, idx, value):
        self.coordinate[idx] = value

    def __getitem__(self, idx):
        return self.coordinate[idx]

    def position(self, coord):
        self.coordinate = copy.deepcopy(coord)



