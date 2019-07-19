
import classad
import collections
import concurrent
import configparser as cp
import datetime
import htcondor
import logging
import os
import sys
import time

from contextlib import contextmanager

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

logger = logging.getLogger(__name__)

class Local(Executor):

    def _core_optimization(self, handler, particles):

        if self._workers > 1:
            logger.error('local parallel not supported yet')
            sys.exit(1)

        # create pool to execute local jobs
        with concurrent.future.ProcessPoolExecutor(max_workers=self._workers) as executor:

            # get iterable from searchspace dict
            it_rootdir = os.path.join(self._root_dir, 'iteration_{}'.format(it))
            os.makedirs(it_rootdir)

            iterator = []
            for sp, job in self._sps.items():
                iterator.append(tuple(it_rootdir, ))

            executor.map(func_wrapper, rootdir, agentid, kwargs)

    def _wait(self):
        raise NotImplementedError
