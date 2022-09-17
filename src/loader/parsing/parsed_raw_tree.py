from typing import List

from .parsed_child import ParsedChild


class ParsedRawTree:
    def __init__(self, children: List[ParsedChild]):
        self._children = children

    @property
    def children(self):
        return self._children
