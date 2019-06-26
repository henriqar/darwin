
import collections
import concurrent
import datetime
import logging
import os
import sys

from darwin.dlogger import dlogger
from darwin.dsl.constants import constants as cnts

from darwin.engine.opt.agents.agent import agent

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

__log = logging.getLogger('darwin')

# context in strategy pattern
class executor():

    # define single instance (singleton)
    __instance = None

    # define the arbiter for jobs executed
    # ARBITER = cnts.ROUND_ROBIN

    def __new__(cls):
        if executor.__instance is None:
            executor.__instance = super().__new__(cls)
        return executor.__instance


    def __init__(self, func, engine, procs=1, timeout=None):

        # save the func to be executed
        self._func = func

        # create the dictionary responsible to hold all registered searchspaces
        self._jobs = collections.deque()

        # create a threadpool for local execution with max_workreers as
        # set by the user
        self._workers = procs

        # save timeout for job
        self._timeout = timeout

        # stretegy reference
        self._strategy = None


    # def register_searchspace(self, spid):

    #     # register searchspace using its id
    #     self._sps[spid] = []

    def register_strategy(self, strategy):

        # register strategy instance (one at a time)
        self._strategy = strategy

    def register_job(self, agent_ref, job):

        # add job to dict of agents
        self._jobs.append((agent_ref, job))

    def _local_execute(self, it):

        if self.workers > 1:
            __log.error('local parallel not supported yet')
            sys.exit(1)

        # create pool to execute local jobs
        with concurrent.futures.ProcessPoolExecutor(max_workers=self._workers) as executor:

            # get iterable from searchspace dict
            it_rootdir = os.path.join(self._root_dir, 'iteration_{}'.format(it))
            os.makedirs(it_rootdir)

            iterator = []
            for sp, job in self._sps.items():
                iterator.append(tuple(it_rootdir, ))

            executor.map(func_wrapper, rootdir, agentid, kwargs)

    def _cluster_execute(self):

        # send workers to cluster
        # monitor all jobs
        # after all jobs end send func call to get values

        # a = map_async(self, func, iterable, chunksize=None, callbakc=None, error_callback=None)
        # a.wait(timeout)
        pass
