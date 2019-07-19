
from importlib import import_module

from .executor import Executor

def factory(execname, *args, **kwargs):

    try:
        module = execname.lower()
        exec_ = import_module('.' + module, package='darwin.engine.executors')
        class_ = getattr(exec_, execname)

        instance = class_(*args, **kwargs)
    except (AttributeError, ImportError):
        raise ImportError('{} is not a child of executor'. format(execname))
    else:
        if not issubclass(class_, Executor):
            raise ImportError('there is no {} executor implemented')

    return instance
