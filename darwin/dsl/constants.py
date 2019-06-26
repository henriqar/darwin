
class constants:

    _LOCAL = 0
    _HTCONDOR = 1

    _ROUND_ROBIN = 2
    _FIFO = 3
    _STACK = 4

    @property
    def LOCAL(self):
        return type(self)._LOCAL

    @property
    def HTCONDOR(self):
        return type(self)._HTCONDOR

    @property
    def ROUND_ROBIN(self):
        return type(self)._ROUND_ROBIN

    @property
    def FIFO(self):
        return type(self)._FIFO

    @property
    def STACK(self):
        return type(self)._STACK
