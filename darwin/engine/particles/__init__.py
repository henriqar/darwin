
from .particle_universe import ParticleUniverse

# import re

# from importlib import import_module


# def factory(optm, *args, **kwargs):

#     try:
#         regex = r'[A-Z][^A-Z]*'
#         module = '_'.join([x.lower() for x in re.findall(regex, optm)])

#         exec_ = import_module('.' +  module, package='darwin.engine.particles')
#         class_ = getattr(exec_, optm)

#         instance = class_(*args, **kwargs)
#     except ImportError:
#         instance = Particle(*args, **kwargs)
#     except AttributeError:
#         raise ImportError('{} is not a child of particle'.format(optm))
#     else:
#         if not issubclass(class_, Particles):
#             raise ImportError('there is no {} particle implemented')

#     Particle.add_instance(instance)
#     return instance
