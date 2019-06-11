
class node:

    def __init__(self, p):

        # get the P set with excluded values
        self._p = set(p)

        # set the node weight
        self._w = 0

        # childs of the node
        self._childs = []

    @property
    def p(self):
        return self._p

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, val):
        self._w = val

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
