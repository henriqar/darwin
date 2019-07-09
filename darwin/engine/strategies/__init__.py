

from importlib import import_module

from .strategy import Strategy

from darwin._constants import opt

def factory(*args, **kwargs):

    name = args[0].optimization

    try:

        if not hasattr(opt, name):
            raise ValueError('unexpected strategy value "{}"'.format(name))
        else:
            module_name = name.lower()
            class_name = name.lower().capitalize()

        strategy_module = import_module('.' + module_name,
                package='darwin.engine.strategies')
        strategy_class = getattr(strategy_module, class_name)

        instance = strategy_class(*args, **kwargs)

    except (AttributeError, ImportError):
        raise ImportError('{} is not a child of strategy'. format(name))
    else:
        if not issubclass(strategy_class, Strategy):
            raise ImportError('there is no {} strategy implemented')

    return instance
