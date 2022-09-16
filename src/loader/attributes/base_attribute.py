from abc import ABC, abstractmethod

from ..parsing.parsed_attribute import ParsedAttribute


class BaseAttribute(ABC):
    def __init__(self, parsed_attribute: ParsedAttribute):
        self._parsed_attribute = parsed_attribute

    @abstractmethod
    def run(self):
        pass
