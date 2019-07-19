
import re

from importlib import import_module

from .strategy import Strategy

def factory(optm, *args, **kwargs):

    try:
        regex = r'[A-Z][^A-Z]*'
        module = '_'.join([x.lower() for x in re.findall(regex, optm)])

        exec_ = import_module('.' + module, package='darwin.engine.strategies')
        class_ = getattr(exec_, optm)

        instance = class_(*args, **kwargs)
    except (AttributeError, ImportError):
        raise ImportError('{} is not a child of strategy'. format(optm))
    else:
        if not issubclass(class_, Strategy):
            raise ImportError('there is no {} strategy implemented')

    return instance
