
import classad
import collections
import concurrent
import datetime
import htcondor
import logging
import os
import sys
import time

from configparser import NoSectionError, NoOptionError
from contextlib import contextmanager

from . import Executor

@contextmanager
def agent_dir(child):

    parent_dir = os.getcwd()
    try:
        os.chdir(child)
        yield child
    finally:
        os.chdir(parent_dir)

_log = logging.getLogger(__name__)

# context in strategy pattern
class Htcondor(Executor):

    _JOB_IDLE = 0
    _JOB_RUNNING = 1
    _JOB_REMOVED = 2
    _JOB_COMPLETED = 3
    _JOB_HELD = 4
    _JOB_TRANSFERING_OUTPUT = 5
    _JOB_SUSPENDED = 6

    def _prepare_job_args(self):
        pass

    def _evaluate(self, curr_dir):

        for clusterid, v in self._job_ref.items():

            agent_ref, ads, agent_dir_name = v
            with agent_dir(os.path.join(curr_dir, agent_dir_name)) as child:

                # call retrieve ads from htcondor in this directory
                # self._schedd.retrieve("ClusterId == %d".format(clusterid))

                # call function to extract fitness value from execution
                agent_ref.intermediate = self._func()

    def _execute(self, curr_dir):

        # secure the joib id from condor
        self._job_ref = {}

        index = 0
        while self._jobs:

            # pop value and get agent ref and args for it
            agent, arg = self._jobs.pop()

            arguments = ' '.join('-%s %s' % tup for tup in arg.items())
            self._submitf['htcondor']['arguments'] = arguments

            agent_dir_name = 'agent_' + str(index)
            agent_dir = os.path.join(curr_dir, agent_dir_name)
            os.makedirs(agent_dir)
            self._submitf['htcondor']['initialdir'] = agent_dir

            # get redirect of htcondor submit file to a dict
            sub = htcondor.Submit(dict(self._submitf.items('htcondor')))

            with self._schedd.transaction() as txn:
                ads = []
                clusterid = sub.queue(txn)
                # clusterid = sub.queue(txn, ad_results=ads)
                self._job_ref[clusterid] = (agent, ads, agent_dir_name)
                # self._schedd.spool(ads)

            # increment index
            index += 1

    def _wait(self):

        # config parser handler
        conf = self._submitf

        try:
            refresh_rate = int(conf['darwin']['refresh_rate'])
        except (NoSectionError, NoOptionError) as e:
            # default refresh in seconds
            refresh_rate = 60

        it = iter(self._job_ref.keys())
        req_string = '(ClusterId == {})'.format(next(it))
        for i in it:
            req_string += ' || (ClusterId == {})'.format(i)

        finished = False
        while not finished:

            # query schedd for all job procs
            query = self._schedd.xquery(
                    requirements=req_string,
                    projection=['ProcId', 'ClusterId', 'JobStatus'])

            try:
                data = next(query)
            except StopIteration:
                finished = True

            # wait to probe condor again
            time.sleep(refresh_rate)

