
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

logger = logging.getLogger(__name__)

# context in strategy pattern
class Htcondor(Executor):

    _JOB_IDLE = 0
    _JOB_RUNNING = 1
    _JOB_REMOVED = 2
    _JOB_COMPLETED = 3
    _JOB_HELD = 4
    _JOB_TRANSFERING_OUTPUT = 5
    _JOB_SUSPENDED = 6

    # def __init__(self, data, filename, procs=1, timeout=None):

    #     # call super constructor
    #     super().__init__(data, filename, procs=procs, timeout=timeout)

    #     # get the scheduler
    #     self._schedd = htcondor.Schedd()

    # def _evaluate(self, jobdict):

    #     for clusterid, v in jobdict.items():

    #         agent_ref, ads, agent_dir_name = v
    #         with agent_dir(os.path.join(curr_dir, agent_dir_name)) as child:

    #             # call retrieve ads from htcondor in this directory
    #             # self._schedd.retrieve("ClusterId == %d".format(clusterid))

    #             # call function to extract fitness value from execution
    #             agent_ref.intermediate = self._func()

    #             if agent_ref.intermediate < 0:
    #                 logger.error('negative fitness value found: {}'.format(
    #                     agent_ref.intermediate))
    #                 sys.exit(1)

    def _execute(self, handler):

        schedd = htcondor.Schedd()

        # config parser handler
        conf = self._submitf

        # secure the joib id from condor
        ids = []

        length = len(self._jobs)
        for idx in range(length):

            # pop value and get args for it
            arg = self._jobs.popleft()

            arguments = ' '.join('-%s %s' % tup for tup in arg.items())
            conf['htcondor']['arguments'] = arguments
            conf['htcondor']['initialdir'] = handler.agentpathlist[idx]

            # get redirect of htcondor submit file to a dict
            sub = htcondor.Submit(dict(conf.items('htcondor')))

            with schedd.transaction() as txn:
                ads = []
                # clusterid = sub.queue(txn)
                clusterid = sub.queue(txn, ad_results=ads)
                ids.append(clusterid)
                # jobdict.append(clusterid] = (ads)
                # self._schedd.spool(ads)

        try:
            refresh_rate = int(conf['darwin']['refresh_rate'])
        except (NoSectionError, NoOptionError) as e:
            # default refresh in seconds
            refresh_rate = 60

        req = ' || '.join('(ClusterId == {})'.format(id) for id in ids)
        finished = False
        while not finished:

            # query schedd for all job procs
            query = schedd.xquery(
                    requirements=req,
                    projection=['ClusterId', 'JobStatus'])

            try:
                data = next(query)
            except StopIteration:
                finished = True
            else:
                # wait to probe condor again
                time.sleep(refresh_rate)

    #             # call retrieve ads from htcondor in this directory
    #             # self._schedd.retrieve("ClusterId == %d".format(clusterid))

