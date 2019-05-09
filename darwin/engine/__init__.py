
import platform

from .execution.local import local

if platform.system == 'Linux':
    from .execution.clustering import clustering

