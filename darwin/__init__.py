
from .dsl import Algorithm
from .dsl import Formatter

from ._constants import drm
from ._constants import opt

import logging
import pkg_resources

__version__ = pkg_resources.require("darwin")[0].version
print('darwin v{}'.format(__version__))

_log = logging.getLogger(__name__)

# set log level
_log.setLevel(logging.ERROR)

# instantiate and create the project logger
_cmd_handler = logging.StreamHandler()
_file_handler = logging.FileHandler('darwin.log')

_cmd_handler.setLevel(logging.ERROR)
_file_handler.setLevel(logging.INFO)

_cmd_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - '
        '%(levelname)s - %(message)s'))

# add handlers to logger
_log.addHandler(_cmd_handler)
_log.addHandler(_file_handler)

# constants.ROUND_ROBIN = 2
# constants.FIFO = 3
# constants.STACK = 4
