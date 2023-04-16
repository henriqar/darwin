
import abc
import configparser
import collections
import logging
import os
import shutil
import sys
import time
import shutil
import datetime
import signal

import darwin.engine.particles as particles

from darwin.constants import drm

AUTO_SUBMIT_FILE = \
"""
[darwin]
 executable=autoexecutor
 refresh_rate=3
 #exec_time=60

 [htcondor]
 universe=vanilla
 error=err.$(ClusterId)
 output=out.$(ClusterId)
 log=log.$(ClusterId)
 #should_transfer_files = YES
"""

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

    class Context():
        def __init__(self, iteration, config):
            self.iteration = iteration
            self.root = os.getcwd()
            self.env = os.path.join(self.root, config.env)
            self.optdir = os.path.join(self.root, config.optdir)
            # self.iteration = 'initial'

            if not os.path.exists(self.optdir):
                logger.error('cannot find the optimization directory specified')
                sys.exit(1)

        @property
        def iterationpath(self):
            return os.path.join(self.env, 'iteration_{}'.format(self.iteration))

        def particlepath(self, name):
            return os.path.join(self.iterationpath, name)

        def __enter__(self):
            for p in particles.particles():
                copyas(self.optdir, self.particlepath(p.name))
            return self

        def __exit__(self, *exec_details):
            # particles.evaluate(self.iterationpath, self.strategy)
            pass

    def __init__(self, config, use_auto_submit):

        # verify if submit file exists
        if not os.path.isfile(config.submitfile):
            logger.error('file "{}" not found'.format(config.submitfile))
            sys.exit(1)

        # save the config
        self.config = config
        self.submitf = configparser.ConfigParser()

        if not use_auto_submit:
            # get the submit file for the darwin application
            self.submitf.read(config.submitfile)
        else:
            logger.info("Using auto submit file")
            self.submitf.read_string(AUTO_SUBMIT_FILE)

        # stretegy reference
        self.strategy = None

        # create signal interrup
        signal.signal(signal.SIGINT, self._delegateInterruptHandler)

    def setStrategy(self, strategy):
        self.strategy = strategy

    def _delegateInterruptHandler(self, signum, frame):
        try:
            self._interruptHandler()
        finally:
            sys.exit(1)

    @abc.abstractmethod
    def _interruptHandler(self):
        logger.info('application finished via SIGINT or SIGKILL')
        sys.exit(1)

    @abc.abstractmethod
    def _coreExecution(self, handler, particles):
        raise NotImplementedError

    @abc.abstractmethod
    def _cleanUp(self):
        raise NotImplementedError

    @exectime('Total optimization time is')
    def optimize(self):

        if os.path.exists(self.config.env) and  os.path.isdir(self.config.env):
            shutil.rmtree(self.config.env, ignore_errors=True)

        for iteration in self.strategy.iterations():
            with Executor.Context(iteration, self.config) as handler:
                self._coreExecution(handler, particles.particles())
                particles.evaluate(handler.iterationpath, self.strategy)
                # self.strategy.fitnessEvaluation()

        # set cleanUp to clean executors garbage left
        self.strategy.cleanUp()
        self._cleanUp()







