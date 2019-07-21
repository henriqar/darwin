
import logging

from ._algorithm import Algorithm
from .dsl import Formatter

from ._constants import drm
from ._constants import opt

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# instantiate and create the project logger
_cmd = logging.StreamHandler()
_file = logging.FileHandler(filename='darwin.log')

_cmd.setLevel(logging.WARNING)
_file.setLevel(logging.INFO)

_cmd.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
_file.setFormatter(logging.Formatter('%(asctime)s - %(name)s - '
        '%(levelname)s - %(message)s'))

# add handlers to logger
logger.addHandler(_cmd)
logger.addHandler(_file)

