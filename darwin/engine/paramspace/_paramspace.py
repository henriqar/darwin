
from ._node import node

class paramspace:

    def __init__(self):

        # create the dictionary to hold all sets
        # each set will be indexed by and id, created using the name of the
        # parameter. The parameters will be automatically mapped to a discrete
        # integer value on the parameter_map
        self._params = {}

        # define the auto incremented parameter id
        self._param_id = 0

        # create the list of exclusive groups
        self._exclusive_groups = []

        # save the tree root node
        self._tree_root = None

    def __item__(self, idx):
        return self._params[idx]

    def add_param(self, name=None, param=None, discrete=False):

        if name is None or name == '':
            raise TypeError("param name must be defined, got '{}'".format(name))

        if isinstance(param, tuple):
            # force mapparam to be tuple, not modifyable
            self._params[self._param_id] = (name, param)
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
        self._tree_root = node(tuple([i for i in range(self._param_id)]))

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

        while nodes:

            tnode = nodes.pop()

            w = 1
            for pi in tuple(tnode.p):
                w *= self._param_weight(pi)

            tnode.w = w

            if tnode.size > 0:
                for child in reversed(range(tnode.size)):
                    nodes.append(tnode[child])

    def _param_weight(self, idx):
        if idx in self._params:
            _, v = self._params[idx]
            return len(v)
        return 0


    def __repr__(self):

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
            # print(lcprefix, end='')
            # print(tnode.p)
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

