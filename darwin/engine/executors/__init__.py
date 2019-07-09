
from importlib import import_module

from .executor import Executor

from darwin._constants import drm

def factory(*args, **kwargs):

    data = args[0]
    name = data.executor

    try:

        if not hasattr(drm, name):
            raise ValueError('unexpected executor value "{}"'.format(name))
        else:
            module_name = name.lower()
            class_name = name.lower().capitalize()

        executor_module = import_module('.' + module_name,
                package='darwin.engine.executors')
        executor_class = getattr(executor_module, class_name)

        instance = executor_class(*args, **kwargs)

    except (AttributeError, ImportError):
        raise ImportError('{} is not a child of executor'. format(name))
    else:
        if not issubclass(executor_class, Executor):
            raise ImportError('there is no {} executor implemented')

    return instance
