"""
Maps a parsed file into its component equivalent
"""
from ..parsing import ParsedFile


class Mapper:
    def __init__(self, parsed_file: ParsedFile):
        self._parsed_file = parsed_file
