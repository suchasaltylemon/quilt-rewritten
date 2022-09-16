from bs4 import Tag

from .parsed_child import ParsedChild
from .parser import IParser


class ChildParser(IParser):
    SPECIAL_ATTRIBUTES = ["class"]

    def __init__(self, tag: Tag):
        self._tag = tag

    def parse(self):
        tag_name = self._tag.name
        tag_attributes = {k: v for k, v in self._tag.attrs.items() if k not in ChildParser.SPECIAL_ATTRIBUTES}
        tag_class = self._tag["class"][0] if self._tag.has_attr("class") else None

        children = [ChildParser(child).parse() for child in self._tag.children if type(child) is Tag]

        return ParsedChild(tag_name, tag_attributes, children, tag_class)
