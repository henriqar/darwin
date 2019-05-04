
class constants:

    _LOCAL = 0
    _HTCONDOR = 1

    @property
    def LOCAL(self):
        return type(self)._LOCAL

    @property
    def HTCONDOR(self):
        return type(self)._HTCONDOR
