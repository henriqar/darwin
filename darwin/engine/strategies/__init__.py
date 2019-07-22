
import re
import logging
import sys

from importlib import import_module

from .strategy import Strategy

logger = logging.getLogger(__name__)

def factory(optm, *args, **kwargs):

    try:
        regex = r'[A-Z][^A-Z]*'
        module = '_'.join([x.lower() for x in re.findall(regex, optm)])

        exec_ = import_module('.' + module, package='darwin.engine.strategies')
        class_ = getattr(exec_, optm)

        instance = class_(*args, **kwargs)
    except (AttributeError, ImportError):
        logger.error('{} is not a child of strategy'. format(optm))
        sys.exit(1)
    else:
        if not issubclass(class_, Strategy):
            logger.error('there is no {} strategy implemented')
            sys.exit(1)

    return instance
