from abc import abstractmethod, ABC


class IParser(ABC):
    @abstractmethod
    def parse(self):
        pass
