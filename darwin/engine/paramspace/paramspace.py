
import logging
import numpy as np

from types import MappingProxyType

import darwin.engine.opt.searchspaces as sp

from .map import Map
from .node import Node


logger = logging.getLogger(__name__)

class Paramspace:

    # create the singleton pattern
    __instance = None

    def __new__(cls):
        if Paramspace.__instance is None:
            Paramspace.__instance = super().__new__(cls)
        return Paramspace.__instance

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
        self._tree_root = None
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

    def add_param(self, name, param, formatter, discrete):

        if isinstance(param, tuple):

            # create map
            if formatter is not None:
                m = Map(param, discrete, formatter=formatter)
            else:
                m = Map(param, discrete)

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
        self._tree_root = Node(tuple([i for i in range(self._param_id)]))

        # build random space using the tree structure
        for ex in self._exclusive_groups:

            nodes = [self._tree_root]
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
        nodes = [self._tree_root]

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

    def create_searchspaces(self, opt_alg, kwargs):

        # create a list of searchspaces basd on the parameters found
        searchspaces = []
        for params in self._pt:

            # searchspace aux
            spaux = sp.factory(opt_alg, **kwargs)
            # spaux = spfactory.create_searchspace(opt_alg, kwargs)
            spaux.n = params
            spaux.set_paramspace(self)

            searchspaces.append(spaux)

        return searchspaces

    def _param_weight(self, idx):
        if idx in self._params:
            _, v = self._params[idx]
            return len(v)
        return 0


    def __str__(self):

        string = []
        nodes = [self._tree_root]

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

    def random_uniform(self):

        # create dict to hold parameters
        pdict = {}

        # choose one of the possibilities
        choosen = np.random.choice(self._pt, p=self._wp)

        # get item and randomize arguments inside
        for param in choosen:
            name, tup = self._params[param]
            pdict[name] =  np.random.choice(tup)

        # return read-only dict for user
        return MappingProxyType(pdict)

    def random_gaussian(self):

        # create dict to hold parameters
        pdict = {}


        # return read-only dict for user
        return MappingProxyType(pdict)

    def random_cauchy(self):

        # create dict to hold parameters
        pdict = {}


        # return read-only dict for user
        return MappingProxyType(pdict)
