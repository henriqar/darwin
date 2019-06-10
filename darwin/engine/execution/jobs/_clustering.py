
import configparser
import os
import platform
import sys

if platform.system() == 'Linux':
    import htcondor
    import classad

from ._job import job

class clustering(job):

    def __init__(self):

        # get the configparser
        self._config = configparser.ConfigParser()

        if not os.path.isfile('DarwinSubmit.ini'):
            print('File "DarwinSubmit.ini" not found, exiting.')
            sys.exit(1)

        # read ini file
        self._config.read('DarwinSubmit.ini')

        # create the htcondor collector
        self._collector = htcondor.Collector(self._config['htcondor'])

        # get the scheduler
        self._sched = htcondor.Schedd()

    def exec(self, func, args):
        return sys.maxsize


