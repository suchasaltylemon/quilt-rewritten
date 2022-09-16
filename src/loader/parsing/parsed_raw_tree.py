from bs4 import BeautifulSoup, Tag

from .child_parser import ChildParser


class ParsedRawTree:
    def __init__(self, html: BeautifulSoup):
        self._html = html
        self._children = [ChildParser(child).parse() for child in self._html.children if type(child) is Tag]

    @property
    def children(self):
        return self._children
