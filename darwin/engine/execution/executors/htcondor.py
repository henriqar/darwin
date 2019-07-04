
import configparser as cp
import collections
import concurrent
import datetime
import logging
import os
import sys
import time

import htcondor
import classad

from contextlib import contextmanager

from darwin.dsl.constants import constants as cnts

from darwin.engine.opt.agents.agent import agent

from . import Executor

@contextmanager
def agent_dir(child):

    parent_dir = os.getcwd()
    try:
        child_path = os.join(parent_dir, child)
        os.chdir(child_path)
        yield child_path
    finally:
        os.chdir(parent_dir)

_log = logging.getLogger('darwin')

# context in strategy pattern
class Htcondor(executor):

    _JOB_IDLE = 0
    _JOB_RUNNING = 1
    _JOB_REMOVED = 2
    _JOB_COMPLETED = 3
    _JOB_HELD = 4
    _JOB_TRANSFERING_OUTPUT = 5
    _JOB_SUSPENDED = 6

    def _evaluate(self, it):

        os.mkdirs(os.join(self._root_dir, it))

        for index, (clusterid, v) in enumerate(self._job_ref.items()):

            agent_ref, ads = v
            with agent_dir(index) as child_path:

                # create child dir
                os.makedirs(child_path)

                # call retrieve ads from htcondor in this directory
                self._schedd.retrieve("ClusterId == %d".format(clusterid))

                # call function to extract fitness value from execution
                agent_ref.intermediate = self._func()

    def _execute(self):

        # secure the joib id from condor
        self._job_ref = {}

        while self._jobs:

            # pop value and get agent ref and args for it
            agent, arg = self._jobs.pop()

            arguments = ' '.join('-%s %s' % tup for tup in arg.items())
            self._submitf['arguments'] = arguments

            # get redirect of htcondor submit file to a dict
            sub = htcondor.Submit(self._submitf['htcondor'])

            with self._schedd.transaction() as txn:
                ads = []
                clusterid = sub.queue(txn, ads)
                self._job_ref[clusterid] = (agent, ads)
                self._schedd.spool(ads)

    def _wait(self):

        # config parser handler
        conf = self._submitf

        try:
            refresh_rate = conf['darwin']['refresh_rate']
        except (cp.NoSectionError, cp.NoOptionError) as e:
            # default refresh in seconds
            refresh_rate = 60

        running_jobs = collections.deque(self._job_ref.keys())
        while running_jobs:

            clusterid = running_jobs.popleft()

            # query schedd for all job procs
            query = self._schedd.xquery(
                    requirements='ClusterId == {}'.format(clusterid),
                    projection=['ProcId', 'ClusterId', 'JobStatus'])

            try:
                data = next(query):
                running_jobs.append(clusterid)
            except StopIteration:
                pass

            # wait to probe condor again
            time.sleep(refresh_rate)

