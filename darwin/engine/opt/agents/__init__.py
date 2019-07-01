
from importlib import import_module

from .agent import Agent

from darwin._constants import opt

def factory(name, *args, **kwargs):

    try:

        if not hasattr(opt, name):
            raise ValueError('unexpected agent value "{}"'.format(name))
        else:
            module_name = name.lower()
            class_name = name.lower().capitalize()

        agent_module = import_module('.' + module_name,
                package='darwin.engine.opt.agents')
        agent_class = getattr(agent_module, class_name)

        instance = agent_class(*args, **kwargs)

    except (AttributeError, ImportError):
        raise ImportError('{} is not a child of agent'. format(name))
    else:
        if not issubclass(agent_class, Agent):
            raise ImportError('there is no {} agent implemented')

    return instance
