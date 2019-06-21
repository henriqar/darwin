
import sys

# from darwin.engine.execution._mediator import mediator
from ._job import job

class local(job):
    def __init__(self, func):

        #call super init
        super().__init__(func)

    # def exec(self, func, args):
    def exec(self, args):
        return func(**args)
