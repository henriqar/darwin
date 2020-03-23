"""
Date: 21/03/2020
"""
import abc
import logging

logger = logging.getLogger(__name__)

class Model(abc.ABC):
    """
    """
    @abc.abstractmethod
    def tojson(self):
        raise NotImplementedError
