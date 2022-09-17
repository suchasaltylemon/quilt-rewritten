from xml.dom.minidom import parseString as minidom, Element

from . import IParser
from .child_parser import ChildParser
from .parsed_raw_tree import ParsedRawTree


class RawTreeParser(IParser):
    def __init__(self, raw_tree_data: str):
        self._raw_tree_data = raw_tree_data

    def parse(self):
        dom = minidom(self._raw_tree_data)

        children = [ChildParser(child).parse() for child in dom.childNodes if type(child) is Element]

        return ParsedRawTree(children)
