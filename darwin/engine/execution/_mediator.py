
import abc

class mediator(abc.ABC):

    @abstractmethod
    def register_job(self, job):
        pass

    @abstractmethod
    def exec_job(self):
        pass

    @abstractmethod
    def register_listener(self):
        pass

    @abstractmethod
    def whisper(self):
        pass
