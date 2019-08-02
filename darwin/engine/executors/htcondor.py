
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
        super().__init__(config)
        try:
            self.refresh_rate = int(self.submitf['darwin']['refresh_rate'])
        except (KeyError, NoSectionError, NoOptionError) as e:
            self.refresh_rate = 60
            logging.warning('refresh_rate not find, fallback to default: 60s')

    def _coreOptimization(self, handler, particles):
        schedd = htcondor.Schedd()
        conf = self.submitf

        executable = conf['darwin']['executable']
        executable_path = os.path.join(handler.optdir, executable)
        conf['htcondor']['executable'] = executable_path
        if not os.path.exists(executable_path):
            logger.error('executable "{}" not found'.format(executable_path))
            sys.exit(1)

        # secure the job id from condor
        ids = []
        for p in particles:
            arguments = p.coordinate.format()
            formatted_args = ['-{} {}'.format(k, v) for k,v in arguments.items()]
            conf['htcondor']['arguments'] = ' '.join(formatted_args)
            conf['htcondor']['initialdir'] = handler.particlepath(p.name)

            # get redirect of htcondor submit file to a dict
            sub = htcondor.Submit(dict(conf.items('htcondor')))
            with schedd.transaction() as txn:
                ads = []
                clusterid = sub.queue(txn, ad_results=ads)
                ids.append(clusterid)
                # self._schedd.spool(ads)

        req = ' || '.join('(ClusterId == {})'.format(id) for id in ids)
        proj = ['ClusterId', 'JobStatus']

        finished = False
        while not finished:
            count = 0
            for data in schedd.xquery(requirements=req, projection=proj):
                count += 1
            if count == 0:
                finished = True
            else:
                time.sleep(self.refresh_rate)

        if 'should_transfer_files' in conf['htcondor'] and \
                conf['htcondor']['should_transfer_files'] in ('YES',):
            for clusterid in ids:
                self._schedd.retrieve("ClusterId == %d".format(clusterid))


