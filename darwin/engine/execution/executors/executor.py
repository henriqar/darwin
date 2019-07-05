

import abc
import collections
import configparser
import htcondor
import logging
import os
import shutil
import sys
import time

from darwin._constants import drm

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

# context in strategy pattern
class Executor(abc.ABC):

    # define single instance (singleton)
    _instance = None

    def __new__(cls, *args, **kwargs):
        if Executor._instance is None:
            Executor._instance = super().__new__(cls)
        return Executor._instance

    def __init__(self, func, method, filename='darwin.submit', procs=1,
            timeout=None):

        # verify if submit file exists
        if not os.path.isfile(filename):
            _log.error('file "{}" not found, exiting.'.format(filename))
            sys.exit(1)

        if method == drm.HTCONDOR:
            # get the scheduler
            self._schedd = htcondor.Schedd()

        # get the submit file for the darwin application
        self._submitf = configparser.ConfigParser()
        self._submitf.read(filename)

        if 'arguments' in self._submitf['htcondor']:
            del self._submitf['htcondor']['arguments']

        if 'initialdir' in self._submitf['htcondor']:
            del self._submitf['htcondor']['initialdir']
            self._submitf['htcondor']['initialdir'] = os.getcwd()

        # define the root dir and the opt dir
        self._root_dir = os.getcwd()
        self._opt_dir = self._root_dir
        self._opt_dir_name = ''

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

        # save executor
        self._method = method

        self._job_ref = {}

    def register_strategy(self, strategy):
        self._strategy = strategy

    def register_job(self, agent_ref, job):
        self._jobs.append((agent_ref, job))

    def _verify_submit_file(self):
        pass

    @abc.abstractmethod
    def _prepare_job_args(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _evaluate(self, curr_dir):
        raise NotImplementedError

    @abc.abstractmethod
    def _execute(self, curr_dir):
        raise NotImplementedError

    @abc.abstractmethod
    def _wait(self):
        raise NotImplementedError

    def _create_environment(self, env='darwin.opt'):

        self._opt_dir = os.path.join(self._root_dir, env)
        self._opt_dir_name = env

        if os.path.exists(self._opt_dir) and os.path.isdir(self._opt_dir):
            # remove dir and create a new one
            shutil.rmtree(self._opt_dir, ignore_errors=True)

        os.makedirs(self._opt_dir)

    def execute(self, searchspaces):

        # create the opt dir and prepare the submit file
        self._prepare_job_args()
        self._create_environment()

        # register executor for every agent
        generators = []
        for sp in searchspaces:
            sp.register_executor(self)
            self._strategy.initializer(sp)

            # create all generators used inside the excution process
            generators.append(self._strategy.execute_step(sp))

        print('-> Runnig initial evaluation')
        iteration = 0

        finished = False
        while not finished:

            #create iteration dir inside opt dir
            curr_dir = os.path.join(self._opt_dir, 'iter_' + str(iteration))
            os.makedirs(curr_dir)

            # execute choosen method (local or cluster)
            self._execute(curr_dir)

            # wait for execution if needed (cluster exec will block here until
            # the results are ready to be collected)
            self._wait()

            # get the results and generate each fitnes in each folder
            # for every agent in every iteration
            self._evaluate(curr_dir)

            # update searchspaces
            for sp in searchspaces:
                sp.update()

            iteration += 1

            try:
                for gen in generators:
                    next(gen)
            except StopIteration:
                finished = True




