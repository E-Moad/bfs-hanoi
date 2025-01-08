from abc import ABC, abstractmethod

class RootedGraph(ABC):
    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def neighbors(self, v):
        pass