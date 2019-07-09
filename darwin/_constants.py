
class _Constants:

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.TypeError('cannot rebind const {}'.format(name))
        self.__dict__[name]=value

    def hasconst(self, const):
        if hasattr(self, const):
            return True
        else:
            return False

drm = _Constants()
opt = _Constants()

drm.LOCAL = 'LOCAL'        # TODO
drm.SEQ_LOCAL = 'SEQ_LOCO' # TODO
drm.HTCONDOR = 'HTCONDOR'

opt.ABC = 'ABC'
opt.ABO = 'ABO'
opt.BA = 'BA'
opt.BHA = 'BHA'
opt.BSA = 'BSA'
opt.BSO = 'BSO'
opt.CS = 'CS'
opt.DE = 'DE'
opt.FA = 'FA'
opt.FPA = 'FPA'
opt.GA = 'GA'
opt.GP = 'GP'
opt.HS = 'HS'
opt.JADE = 'JADE'
opt.LOA = 'LOA'
opt.MBO = 'MBO'
opt.OPT = 'OPT'
opt.PSO = 'PSO'
opt.SA = 'SA'
opt.WCA = 'WCA'

    # _LOCAL = 0
    # _HTCONDOR = 1

    # _ROUND_ROBIN = 2
    # _FIFO = 3
    # _STACK = 4

    # @property
    # def LOCAL(self):
    #     return type(self)._LOCAL

    # @property
    # def HTCONDOR(self):
    #     return type(self)._HTCONDOR

    # @property
    # def ROUND_ROBIN(self):
    #     return type(self)._ROUND_ROBIN

    # @property
    # def FIFO(self):
    #     return type(self)._FIFO

    # @property
    # def STACK(self):
    #     return type(self)._STACK
