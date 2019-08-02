
import re
import subprocess as sp
import collections
import contextlib
import datetime
import logging
import os
import sys
import time

from configparser import NoSectionError, NoOptionError

from . import Executor

logger = logging.getLogger(__name__)

@contextlib.contextmanager
def _parallelContext(comm, cores):
    try:
        default = sp.run([comm, '-S'], stdout=sp.PIPE, universal_newlines=True)
        default_cores = default.stdout
        sp.run([comm, '-S {}'.format(cores)])
        yield
        sp.run([comm, '-S {}'.format(default_cores)])
    except sp.CalledProcessError:
        logger.error('taskspooler failed to set number of cores')
        sys.exit(1)

# context in strategy pattern
class TaskSpooler(Executor):

    class JobEntry():
        def __init__(self, state, output, times):
            self.state = state
            self.output = output
            self.times = times

    def __init__(self, config):
        super().__init__(config)
        try:
            self.refresh_rate = int(self.submitf['darwin']['refresh_rate'])
        except (KeyError, NoSectionError, NoOptionError) as e:
            self.refresh_rate = 60
            logging.warning('refresh_rate not find, fallback to default: 60s')

        if sys.platform == 'linux' or sys.platform == 'linux2':
            self.comm = 'tsp'
        elif sys.platform == 'darwin':
            self.comm = 'ts'

        self.regex = re.compile(r"""^(\d+)\s+               # job id
                                     ([a-z]+)\s+            # state
                                     ([\a-zA-Z0-9_\.]+)\s+  # output file
                                     (\d+)\s+               # e-level
                                     (.+/.+/.+)\s+          # time (r/u/s)
                                     .+$""", re.X)

    def _cmdPrepare(self, dictarg):
        result = []
        for k,v in dictarg.items():
            result.append('-{}'.format(k))
            result.append(v)
        return result

    def _coreOptimization(self, handler, particles):

        conf = self.submitf
        executable = conf['darwin']['executable']
        executable_path = os.path.join(handler.optdir, executable)
        if not os.path.exists(executable_path):
            logger.error('executable "{}" not found'.format(executable_path))
            sys.exit(1)

        with _parallelContext(self.comm, self.config.parallelism):
            ids = []
            for p in particles:
                arguments = p.coordinate.format()
                arguments['root'] = '{}'.format(handler.particlepath(p.name))
                args = self._cmdPrepare(arguments)
                jid = self._cmdSchedule(executable_path, args)
                ids.append(jid)
            while ids:
                for jid in ids:
                    state = self._cmdJobState(jid)
                    if state == "finished":
                        ids.remove(jid)
                        self._cmdClearJob(jid)
                time.sleep(self.refresh_rate)

    def _cmdUpdateJobs(self):
        try:
            # ts -l show the current job list
            jobs = {}
            comm = [self.comm, '-l']
            with sp.Popen(comm, stdout=sp.PIPE, universal_newlines=True) as pd:
                out, err = pd.communicate()
                lines = re.split(r'\n', out)
                for line in filter(None, lines[1:]):
                    aux = self.regex.findall(line)
                    id, state, output, _, times = aux[0]
                    if int(id) in self.jobs:
                        jobs[int(id)].state = state
                        jobs[int(id)].times = times
                    else:
                        jobs[int(id)] = TaskSpooler.JobEntry(state, output, times)
                    return jobs
        except subprocess.CalledProcessError:
            logger.error('something went wrong in tsp execution @cmdUpdateJobs')
            sys.exit(1)

    def _cmdJobState(self, jid):
        try:
            state = sp.run([self.comm, '-s {}'.format(jid)], stdout=sp.PIPE,
                    universal_newlines=True)
            return state.stdout.strip()
        except sp.CalledProcessError:
            logger.error('taskspooler state runtime error')
            sys.exit(1)

    def _cmdSchedule(self, executable, inputs):
        try:
            comm = [self.comm, executable]
            comm.extend(inputs)
            with sp.Popen(comm, stdout=sp.PIPE, universal_newlines=True) as pd:
                out, err = pd.communicate()
                return int(out)
        except sp.CalledProcessError:
            logger.error('something went wrong in tsp execution @cmdSchedule')
            sys.exit(1)

    def _cmdClearJob(self, jid):
        try:
            sp.run([self.comm, '-r {}'.format(jid)])
        except sp.CalledProcessError:
            logger.error('taskspooler clear runtime error')
            sys.exit(1)

