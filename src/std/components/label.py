from .component import Component
from ..text_element import ITextElement


class Label(Component, ITextElement):
    @property
    def display_text(self):
        return ""

    @property
    def name(self):
        return ""
