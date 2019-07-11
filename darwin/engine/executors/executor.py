
import abc
import configparser
import contextlib
import collections
import htcondor
import logging
import os
import shutil
import sys
import time
import shutil

from darwin._constants import drm

@contextlib.contextmanager
def agentwd(child):

    parent_dir = os.getcwd()
    try:
        os.chdir(child)
        yield child
    finally:
        os.chdir(parent_dir)

logger = logging.getLogger(__name__)

def copyas(src, dst):
    if not os.path.isabs(src):
        raise RuntimeError('src is not an abs path')
    names = os.listdir(src)
    os.makedirs(dst)
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copyas(srcname, dstname)
            else:
                os.symlink(srcname, dstname)
        except OSError as why:
            errors.append((srcname, dstname, str(why)))
        except Error as why:
            errors.extend(err.args[0])
    try:
        shutil.copystat(src, dst)
    except OSError as  why:
        if why.winerror is None:
            errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)


class Executor(abc.ABC):

    class ContextHandler():

        def __init__(self, func, searchspace, optdir='darwin.opt', env='darwin.exec'):

            self._root = os.getcwd()
            self._execdir = os.path.join(self._root, env)
            self._optdir = os.path.join(self._root, optdir)

            self._iteration = os.path.join(self._execdir, 'iteration_initial')

            data = []
            for idx in range(searchspace.m):
                data.append('agent_{}'.format(idx))
            self._agents = tuple(data)

            self._searchspace = searchspace
            self._func = func

        @property
        def rootpath(self):
            return self._root

        @property
        def execdirpath(self):
            return self._execdir

        @property
        def optdirpath(self):
            return self._optdir

        @property
        def iteration(self):
            return self._iteration

        @iteration.setter
        def iteration(self, it):
            self._iteration = it

        @property
        def iterationpath(self):
            return os.path.join(self._execdir, 'iteration_' + str(self._iteration))

        @property
        def agentpathlist(self):
            itpath = self.iterationpath
            return tuple(os.path.join(itpath, agent) for agent in self._agents)

        def __enter__(self):

            # get all agent paths, create folders and symbolic link to
            # original files
            for agentpath in self.agentpathlist:
                copyas(self._optdir, agentpath)

            return self

        def __exit__(self, *exec_details):

            # execute all agents evaluation
            for idx, agentdir in enumerate(self.agentpathlist):
                logger.info('changed to wd "{}"'.format(agentdir))
                os.chdir(agentdir)
                instantfit = self._func()
                if instantfit < 0:
                    logger.error('negative fitness value found: {}'.format(
                        instantfit))
                    sys.exit(1)

                logger.info('iter: {} agent: {} fit: {} dir: {}'.format(
                    self.iteration, idx, instantfit, agentdir))
                self._searchspace.a[idx].fit = instantfit

            # on exit return to root folder
            os.chdir(self._root)
            self._searchspace.update()

    # define single instance (singleton)
    _instance = None

    def __new__(cls, *args, **kwargs):
        if Executor._instance is None:
            Executor._instance = super().__new__(cls)
        return Executor._instance

    def __init__(self, data, filename, procs=1, timeout=None):

        # verify if submit file exists
        if not os.path.isfile(filename):
            logger.error('file "{}" not found, exiting.'.format(filename))
            sys.exit(1)

        # get the submit file for the darwin application
        self._submitf = configparser.ConfigParser()
        self._submitf.read(filename)

        # save the func to be executed
        self._func = data.func

        # create the dictionary responsible to hold all registered searchspaces
        self._jobs = collections.deque()

        # save timeout for job
        self._timeout = timeout

        # stretegy reference
        self._strategy = None


    def register_strategy(self, strategy):
        self._strategy = strategy

    def register_job(self, job):
        self._jobs.append(job)

    @abc.abstractmethod
    def _execute(self, handler):
        raise NotImplementedError

    def execute(self, searchspace):

        # register executor for every agent
        searchspace.register_executor(self)
        self._strategy.initializer(searchspace)

        # create all generators used inside the excution process
        generator = self._strategy.step(searchspace)

        # create path object to handle multiple paths
        handler = Executor.ContextHandler(self._func, searchspace)

        if not os.path.exists(handler.optdirpath):
            logger.error('an optdir containing all optimization files must be',
                    ' provided')
            sys.exit(1)

        # create the opt dir and prepare the submit file
        if os.path.exists(handler.execdirpath) and \
                os.path.isdir(handler.execdirpath):
            shutil.rmtree(handler.execdirpath, ignore_errors=True)

        handler.iteration = 'inital'
        with handler:
            print('Evaluating random initialization of searchspace\n')
            self._execute(handler)

        # iteration = 0
        finished = False
        while not finished:

            try:
                handler.iteration = next(generator)
            except StopIteration:
                searchspace.global_fitness()
                finished = True
            else:
                with handler:
                    self._execute(handler)





