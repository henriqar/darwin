
import os
import platform
import sys
import re

if platform.system() == 'Linux':
    import htcondor
    import classad

from ._job import job

from darwin.dlogger import dlogger

class clustering(job):

    def __init__(self, func, filename='darwin.submit'):

        #call super init
        super().__init__(func)

        if not os.path.isfile(filename):
            dlogger.error('File "{}" not found, exiting.'.format(filename))
            sys.exit(1)

        # get the scheduler
        self._sched = htcondor.Schedd()

    # def exec(self, func, args):
    def exec(self, args):

        # submit the classad representation of the submit file
        with open(filename) as fp:

            # get the classad iterator for the submit file
            classad_repr = classad.parseAds(fp)
            jid = self._sched.submit(classad_repr, 1)

        return func()

    def _verify_condor_version(self):

        # software supports version 8.5.6 and above
        supported_ver = '8.5.6'

        r = re.search(r'\d\.\d\.\d', htcondor.version())
        if r is not None and r.group(0) < supported_ver:
            dlogger.error('unsupported htcondor version {}, it must be >= {}'\
                    .format(htcondor.version(), supported_ver))
            sys.exit(1)





