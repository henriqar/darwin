
from importlib import import_module

from .searchspace import Searchspace

from darwin._constants import opt

def factory(name, *args, **kwargs):

    try:

        if not hasattr(opt, name):
            raise ValueError('unexpected searchspace value "{}"'.format(name))
        else:
            module_name = name.lower()
            class_name = name.lower().capitalize()

        searchspace_module = import_module('.' + module_name,
                package='darwin.engine.opt.searchspaces')
        searchspace_class = getattr(searchspace_module, class_name)

        instance = searchspace_class(*args, **kwargs)

    except (AttributeError, ImportError):
        raise ImportError('{} is not a child of searchspace'. format(name))
    else:
        if not issubclass(searchspace_class, Searchspace):
            raise ImportError('there is no {} searchspace implemented')

    return instance
