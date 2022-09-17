from abc import ABC
from typing import List

from ..tk_element import ITkElement


class Component(ITkElement, ABC):
    def __init__(self, children: List["Component"]):
        self._children = children
