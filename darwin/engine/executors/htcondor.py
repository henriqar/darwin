
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
class HTCondor(Executor):

    def __init__(self, config):

        # call super constructor
        super().__init__(config)

        try:
            self._refresh_rate = int(self._submitf['darwin']['refresh_rate'])
        except (KeyError, NoSectionError, NoOptionError) as e:
            # default refresh in seconds
            self._refresh_rate = 60
            logging.warning('refresh_rate not find, fallback to default: 60s')

    def _core_optimization(self, handler, particles):

        schedd = htcondor.Schedd()

        # config parser handler
        conf = self._submitf

        executable = conf['darwin']['executable']
        conf['htcondor']['executable'] = os.path.join(handler.optdirpath,
                executable)

        # secure the job id from condor
        ids = []
        for p in particles:

            values = []
            for pos in p.position:
                arg = '-{} {}'.format(pos.name, pos.holding)
                values.append(arg)

            conf['htcondor']['arguments'] = ' '.join(values)
            conf['htcondor']['initialdir'] = handler.particlepath(p.name)

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

