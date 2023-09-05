from abc import ABC, abstractmethod


class AbstractAPICaller(ABC):
    @abstractmethod
    def run_llm(sentence):
        raise NotImplementedError("Abstract method run_llm not implemented")
