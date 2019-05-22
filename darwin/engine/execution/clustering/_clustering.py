
import platform

if platform.system == 'Linux':
    import htcondor
    import classad

class clustering():

    def __init__(self):

        # create the htcondor collector
        self._collector = htcondor.Collector()

        # get the scheduler
        self._sched = htcondor.Schedd()

        # get the submit handle for condor
        self._submit = htcondor.Submit()


