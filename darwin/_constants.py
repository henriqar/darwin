
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

drm.Local = 'Local'        # TODO
drm.HTCondor = 'HTCondor'

opt.ABC = 'ABC'
opt.ABO = 'ABO'
opt.BatAlgorithm = 'BatAlgorithm'
opt.BHA = 'BHA'
opt.BSA = 'BSA'
opt.BSO = 'BSO'
opt.CS = 'CS'
opt.DE = 'DE'
opt.FA = 'FA'
opt.FPA = 'FPA'
opt.GeneticAlgorithm = 'GeneticAlgorithm'
opt.GP = 'GeneticProgramming'
opt.HS = 'HS'
opt.JADE = 'JADE'
opt.LionOptimizationAlgorithm = 'LionOptimizationAlgorithm'
opt.MigratingBirdsOptimization = 'MigratingBirdsOptimization'
opt.OPT = 'OPT'
opt.ParticleSwarmOptimization = 'ParticleSwarmOptimization'
opt.SimulatedAnnealing = 'SimulatedAnnealing'
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
