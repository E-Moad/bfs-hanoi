from abc import ABC, abstractmethod

class RootedRelation(ABC):
    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def actions(self, c):
        pass

    @abstractmethod
    def execute(self, a, c):
        pass
