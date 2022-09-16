from dataclasses import dataclass
from typing import List

from .parsed_raw_tree import ParsedRawTree
from ..attributes.base_attribute import BaseAttribute


@dataclass
class ParsedFile:
    attributes: List[BaseAttribute]
    tree: ParsedRawTree
