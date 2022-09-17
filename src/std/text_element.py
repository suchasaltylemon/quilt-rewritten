from abc import ABC, abstractmethod

from .tk_element import ITkElement


class ITextElement(ITkElement, ABC):
    @abstractmethod
    def display_text(self):
        pass
