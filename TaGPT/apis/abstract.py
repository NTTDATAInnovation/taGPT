from abc import ABC, abstractmethod
from inspect import stack


class AbstractAPICaller(ABC):
    @abstractmethod
    def query(msg):
        raise NotImplementedError(
            f"Abstract method '{stack()[0][3]}' not implemented"
        )
