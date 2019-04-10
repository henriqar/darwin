
import abc

class execution(abc.ABC):

    @abstractmethod
    def register_job (self, job):
        pass

    @abstractmethod
    def exec_jobs(Self):
        pass

    @abstractmethod
    def register_listener(self):
        pass

    @abstractmethod
    def whisper(self):
        pass




