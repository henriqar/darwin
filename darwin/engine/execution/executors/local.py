

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

# def func_wrapper(func, merged_args):

#     # get all argumetns used
#     rootdir, agentid, kwargs = merged_args

#     # lets create the dir to execute the agent and change the thread to
#     # work within this dir
#     agentdir = os.path.join(rootdir, agentid)
#     os.makedirs(agentdir)
#     os.cwd(agentdir)

#     # call the func
#     func(**kwargs)

_log = logging.getLogger(__name__)

class Local(Executor):
    def _prepare_job_args(self):
        raise NotImplementedError

    def _evaluate(self, curr_dir):
        raise NotImplementedError

    def _execute(self, curr_dir):

        if self._workers > 1:
            _log.error('local parallel not supported yet')
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
