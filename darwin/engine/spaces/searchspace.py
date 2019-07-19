
import logging
import numpy as np

from types import MappingProxyType

from darwin.engine.particles import Particle

from .map import Map
from .mapitem import MapItem

logger = logging.getLogger(__name__)

class Searchspace:

    class Node:

        def __init__(self, p):
            self.w = 0          # weight
            self._p = set(p)    # p collection with excluded vars
            self._childs = []

        @property
        def p(self):
            return self._p

        def add_child(self, child):
            if isinstance(child, node):
                self._childs.append(child)

        @property
        def size(self):
            return len(self._childs)

        def __getitem__(self, idx):
            return self._childs[idx]

        def __setitem__(self, idx, val):
            self._childs[idx] = val

        def __str__(self):
            return 'Node(set: {}, weight: {})'.format(self.p, self.w)


    # create the singleton pattern
    __instance = None

    def __new__(cls):
        if Searchspace.__instance is None:
            Searchspace.__instance = super().__new__(cls)
        return Searchspace.__instance

    def __init__(self):

        # each set will be indexed by and id, created using the name of the
        # parameter. The parameters will be automatically mapped to a discrete
        # integer value on the parameter_map
        self._params = {}

        # define the auto incremented parameter id
        self._param_id = 0

        # create the list of exclusive groups
        self._exclusive_groups = []

        # save the tree root node and the reference to the complete param set
        self._treeroot = None
        self._pt = None
        self._wt = None
        self._wp = None

    def __getitem__(self, idx):
        return self._params[idx]

    def __len__(self):
        return self._param_id

    @property
    def n(self):
        return self._param_id

    @property
    def combinations(self):
        return sum(self._wt)

    def _fillparticles(self):

        Particle.set_nullitems([MapItem(*self._params[i]) for i in range(length)])

        for particle in Particle.particles():
            length = self._param_id
            particle.set_position([MapItem(*self._params[i]) for i in range(length)])

    def add_param(self, name, param, formatter, discrete):

        if isinstance(param, tuple):

            # create map
            m = Map(param, discrete, formatter)

            # force mapparam to be tuple, not modifyable
            self._params[self._param_id] = (name, m)
            self._param_id += 1

            return self._param_id - 1
        else:
            raise TypeError("error: map parameter must be a tuple type")

    def add_exclusive_group(self, *groups):

        for group in groups:

            # verify if id of group matches the tuple expected
            if not isinstance(group, tuple):
                raise TypeError('group type "{}" not recognized'.format(group))
            else:
                self._exclusive_groups.append(set(group))

    def build(self):

        # create tree root with all elements
        self._treeroot = Searchspace.Node(tuple([i for i in range(self._param_id)]))

        # build random space using the tree structure
        for ex in self._exclusive_groups:
            nodes = [self._treeroot]
            while nodes:
                tnode = nodes.pop()
                if ex.issubset(tnode.p):
                    if tnode.size > 0:
                        for child in reversed(range(tnode.size)):
                            nodes.append(tnode[child])
                    else:
                        for param in tuple(ex):
                            tnode.add_child(node(tnode.p.difference((param,))))


        # calculate the weights for each branch
        nodes = [self._treeroot]

        leafs = []
        while nodes:
            tnode = nodes.pop()
            w = 1
            for pi in tuple(tnode.p):
                w *= self._param_weight(pi)
            tnode.w = w

            if tnode.size > 0:
                for child in reversed(range(tnode.size)):
                    nodes.append(tnode[child])
            else:
                leafs.append(tnode)

        # create a node correspondin to the space
        self._wt = tuple(map(lambda i: i.w, leafs))
        self._pt = tuple(map(lambda i: tuple(i.p), leafs))

        # set the percentage of each set
        sumw = sum(self._wt)
        self._wp = tuple(map(lambda i: i/sumw, self._wt))

        # fill all particles with values here
        self._fillparticles()

    def _param_weight(self, idx):
        if idx in self._params:
            _, v = self._params[idx]
            return len(v)
        return 0

    def __str__(self):

        string = []
        nodes = [self._treeroot]

        # create prefix list and child prefix list
        prefix = ['']
        cprefix = ['']

        while nodes:

            # get the node to print
            tnode = nodes.pop()

            lprefix = prefix.pop()
            lcprefix = cprefix.pop()
            string.append(lcprefix)
            string.extend([str(tnode.p), '\n'])

            if tnode.size > 0:

                for i in reversed(range(tnode.size)):

                    if i < tnode.size - 1:
                        if tnode[i].size > 0:
                            prefix.append(lprefix + '|   ')
                        else:
                            prefix.append(lprefix + '    ')
                        cprefix.append(lprefix + '|---')
                    else:
                        if tnode[i].size > 0:
                            prefix.append(lprefix + '    ')
                        else:
                            prefix.append(lprefix + '')
                        cprefix.append(lprefix + '`---')

                    nodes.append(tnode[i])

        return ''.join(string)

