from xml.dom.minidom import Element

from .parsed_child import ParsedChild
from .parser import IParser


class ChildParser(IParser):
    SPECIAL_ATTRIBUTES = ["class"]

    def __init__(self, element: Element):
        self._element = element

    def parse(self):
        tag_name = self._element.tagName
        tag_attributes = {k: v for (k, v) in self._element.attributes.items() if
                          k not in ChildParser.SPECIAL_ATTRIBUTES}
        tag_class = self._element.attributes.get("class", None)
        tag_class = tag_class.value if tag_class is not None else None

        children = [ChildParser(child).parse() for child in self._element.childNodes if type(child) is Element]

        return ParsedChild(tag_name, tag_attributes, children, tag_class)
