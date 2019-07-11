
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

from . import Executor

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

    def __init__(self, data, filename, procs=1, timeout=None):

        # call super constructor
        super().__init__(data, filename, procs=procs, timeout=timeout)

        try:
            self._refresh_rate = int(self._submitf['darwin']['refresh_rate'])
        except (KeyError, NoSectionError, NoOptionError) as e:
            # default refresh in seconds
            self._refresh_rate = 60
            logging.warning('refresh_rate not find, fallback to default: 60s')

    def _execute(self, handler):

        schedd = htcondor.Schedd()

        # config parser handler
        conf = self._submitf

        # secure the job id from condor
        ids = []

        length = len(self._jobs)
        for idx in range(length):

            # pop value and get args for it
            arg = self._jobs.popleft()

            executable = conf['darwin']['executable']
            conf['htcondor']['executable'] = os.path.join(handler.optdirpath,
                    executable)

            arguments = ' '.join('-%s %s' % tup for tup in arg.items())
            conf['htcondor']['arguments'] = arguments
            conf['htcondor']['initialdir'] = handler.agentpathlist[idx]

            # get redirect of htcondor submit file to a dict
            sub = htcondor.Submit(dict(conf.items('htcondor')))

            with schedd.transaction() as txn:
                ads = []
                clusterid = sub.queue(txn, ad_results=ads)
                ids.append(clusterid)
                # self._schedd.spool(ads)

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
                time.sleep(self._refresh_rate)

    #             # call retrieve ads from htcondor in this directory
    #             # self._schedd.retrieve("ClusterId == %d".format(clusterid))

