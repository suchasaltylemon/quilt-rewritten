from typing import List

from .attribute_parser import AttributeParser
from .parsed_file import ParsedFile
from .parser import IParser
from .raw_tree_parser import RawTreeParser
from ..attributes import ATTRIBUTE_PREFIX
from ..attributes.base_attribute import BaseAttribute


class FileParser(IParser):
    ROOT_TAG = "<quilt>"
    CLOSED_ROOT_TAG = "</quilt>"

    def __init__(self, file_path: str):
        self._file_path = file_path
        self._stream = open(file_path, 'r')

    def __enter__(self) -> "FileParser":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        self.close()

    def close(self) -> None:
        self._stream.close()

    def parse(self) -> ParsedFile:
        is_root = False
        foreign_attributes: List[BaseAttribute] = []
        root_data = ""

        for line in self._stream:
            if not is_root and line.startswith(ATTRIBUTE_PREFIX):
                attribute_parser = AttributeParser(line)
                foreign_attributes.append(attribute_parser.parse())

            elif line.strip() == FileParser.ROOT_TAG:
                is_root = True

            elif line.strip() == FileParser.CLOSED_ROOT_TAG:
                is_root = False

            elif is_root:
                root_data += line

        raw_tree_parser = RawTreeParser(root_data)
        raw_tree = raw_tree_parser.parse()

        return ParsedFile(foreign_attributes, raw_tree)
