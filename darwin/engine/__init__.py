
import platform

from .execution.local import local
# import darwin.engine.execution.local as local

if platform.system == 'Linux':
    from .execution.clustering import clustering
    # import darwin.engine.execution.clustering._clustering

import darwin.engine.darwinfactory
