
from .agent import agent

class mbo:

    def __init__(self):

        # call base class init
        super().__init__()

        # MBO
        self._nb = [] # array of pointers to neighbours

    @property
    def nb(self):
        return self._nb

    @nb.setter
    def nb(self, nb):
        self._nb = nb


