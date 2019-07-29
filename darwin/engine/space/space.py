
import collections
import logging

from .map import Map

logger = logging.getLogger(__name__)

class Space:
    class Param():
        def __init__(self, name, map):
            self.name = name
            self.map = map

    class Node:
        def __init__(self, p):
            self.w = 0          # weight
            self.p = set(p)    # p collection with excluded vars
            self.childs = []

        def add_child(self, child):
            if isinstance(child, Node):
                self.childs.append(child)

        @property
        def size(self):
            return len(self.childs)

        def __getitem__(self, idx):
            return self.childs[idx]

        def __setitem__(self, idx, val):
            self.childs[idx] = val

        def __str__(self):
            return 'Node(set: {}, weight: {})'.format(self.p, self.w)

    def __init__(self):

        # each set will be indexed by and id, created using the name of the
        # parameter. The parameters will be automatically mapped to a discrete
        # integer value on the parameter_map
        self.params = collections.OrderedDict()

        # define the auto incremented parameter id
        self.id = 0

        # create the list of exclusive groups
        self._exclusive_groups = []

        # save the tree root node and the reference to the complete param set
        self.treeroot = None
        self._pt = None
        self._wt = None
        self._wp = None

    @property
    def dimension(self):
        return self.id

    def __len__(self):
        return sum(self._wt)

    def __getitem__(self, idx):
        return tuple(self.params.items())[idx]

    def axes(self):
        return tuple(self.params.items())

    def addParam(self, name, param, formatter, discrete):
        self.params[self.id] = Space.Param(name, Map(param, discrete, formatter))
        self.id += 1
        return self.id - 1

    def addExclusiveGroup(self, *groups):
        for group in groups:
            self._exclusive_groups.append(set(group))

    def build(self):
        self.treeroot = Space.Node(tuple(range(self.id)))
        nodes = [self.treeroot]

        # build random space using the tree structure
        for ex in self._exclusive_groups:
            nodes = [self.treeroot]
            while nodes:
                tnode = nodes.pop()
                if ex.issubset(tnode.p):
                    if tnode.size > 0:
                        for child in reversed(range(tnode.size)):
                            nodes.append(tnode[child])
                    else:
                        for param in tuple(ex):
                            tnode.add_child(node(tnode.p.difference((param,))))

        leafs = []
        while nodes:
            tnode = nodes.pop()
            w = 1
            for pi in tuple(tnode.p):
                w *= self._paramWeight(pi)
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

    def _paramWeight(self, idx):
        try:
            obj_param= self.params[idx]
            return len(obj_param.map)
        except KeyError:
            return 0

    def __str__(self):

        string = []
        nodes = [self.treeroot]

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

