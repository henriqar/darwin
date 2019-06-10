
import sys

# from darwin.engine.execution._mediator import mediator
from ._job import job

class local(job):

    def exec(self, func, args):
        return func(**args)
