from abc import ABC, abstractmethod


class ITkElement(ABC):
    @abstractmethod
    def name(self):
        pass
