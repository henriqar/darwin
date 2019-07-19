
import abc
import configparser
import collections
import htcondor
import logging
import os
import shutil
import sys
import time
import shutil

from darwin._constants import drm

from darwin.engine.particles import Particle

logger = logging.getLogger(__name__)

def exectime(line):
    def decorator(func):
        def timing(*args, **kwargs):
            start_time = time.time()
            return_value = func(*args, **kwargs)
            run_time = time.time() - start_time
            info = '{} {}'.format(line, datetime.timedelta(seconds=run_time))
            logger.info(info)
            print(info)
            return return_value
        return timing
    return decorator

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

        def __init__(self, optdir='darwin.opt', env='darwin.exec'):
            self._root = os.getcwd()
            self._execdir = os.path.join(self._root, env)
            self._optdir = os.path.join(self._root, optdir)
            self._iteration = 'initial'

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
        def iterationpath(self):
            return os.path.join(self._execdir,
                    'iteration_{}'.format(self._iteration))

        @iterationpath.setter
        def iterationpath(self, it):
            self._iteration = it

        def particlepath(self, name):
            return os.path.join(self.iterationpath, name)

        def __enter__(self):
            # create folders soft linking files to designated particle folders
            for name in Particle.names():
                copyas(self._optdir, self.particlepath(name))
            return self

        def __exit__(self, *exec_details):
            Particle.evaluateall(self.iterationpath)

    # define single instance (singleton)
    _instance = None

    def __new__(cls, *args, **kwargs):
        if Executor._instance is None:
            Executor._instance = super().__new__(cls)
        return Executor._instance

    def __init__(self, config):

        # verify if submit file exists
        if not os.path.isfile(config.submitfile):
            logger.error('file "{}" not found'.format(config.submitfile))
            sys.exit(1)

        # get the submit file for the darwin application
        self._submitf = configparser.ConfigParser()
        self._submitf.read(config.submitfile)

        # create path object to handle multiple paths
        self._handler = Executor.ContextHandler(optdir=config.optdir,
                env=config.execdir)

        # create the dictionary responsible to hold all registered searchspaces
        # self._jobs = collections.deque()

        # save timeout for job
        self._timeout = config.timeout

        # stretegy reference
        self._strategy = None

    def set_strategy(self, strategy):
        self._strategy = strategy

    # def register_job(self, job):
    #     self._jobs.append(job)

    @abc.abstractmethod
    def _core_optimization(self, handler):
        raise NotImplementedError

    @exectime('Total optimization time is')
    def optimize(self):
        handler = self._handler

        # get all particles as tuple
        particles = Particle.particles()

        # register executor for every agent
        self._strategy.initialize(particles)

        # create all generators used inside the excution process
        generator = self._strategy.generator(particles)

        if not os.path.exists(handler.optdirpath):
            logger.error('an optdir containing all optimization files must be',
                    ' provided')
            sys.exit(1)

        # create the opt dir and prepare the submit file
        if os.path.exists(handler.execdirpath) and \
                os.path.isdir(handler.execdirpath):
            shutil.rmtree(handler.execdirpath, ignore_errors=True)

        handler.iteration = 'initial'
        with handler:
            print('Evaluating random initialization of searchspace\n')
            self._core_optimization(handler, particles)

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





