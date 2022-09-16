from bs4 import BeautifulSoup

from . import IParser
from .parsed_raw_tree import ParsedRawTree


class RawTreeParser(IParser):
    def __init__(self, raw_tree_data: str):
        self._raw_tree_data = raw_tree_data

    def parse(self):
        html = BeautifulSoup(self._raw_tree_data, features="html.parser")

        return ParsedRawTree(html)
