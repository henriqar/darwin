
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
import datetime

import darwin.engine.particles as particles

from darwin.constants import drm

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

    def __init__(self, config):

        # verify if submit file exists
        if not os.path.isfile(config.submitfile):
            logger.error('file "{}" not found'.format(config.submitfile))
            sys.exit(1)

        # save the config
        self.config = config

        # get the submit file for the darwin application
        self.submitf = configparser.ConfigParser()
        self.submitf.read(config.submitfile)

        # stretegy reference
        self.strategy = None

    def setStrategy(self, strategy):
        self.strategy = strategy

    @abc.abstractmethod
    def _coreOptimization(self, handler, particles):
        raise NotImplementedError

    @exectime('Total optimization time is')
    def optimize(self):

        if os.path.exists(self.config.env) and  os.path.isdir(self.config.env):
            shutil.rmtree(self.config.env, ignore_errors=True)

        for iteration in self.strategy.iterations():
            with Executor.Context(iteration, self.config) as handler:
                self._coreOptimization(handler, particles.particles())
                self.strategy.fitnessEvaluation()
                particles.evaluate(handler.iterationpath, self.strategy)







