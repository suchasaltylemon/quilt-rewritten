from .parsed_attribute import ParsedAttribute
from .parser import IParser
from ..attributes import ATTRIBUTE_PREFIX


class AttributeParser(IParser):
    def __init__(self, raw_attribute_data: str):
        self._raw_attribute_data = raw_attribute_data.strip()

    def parse(self):
        prefixless_data = self._raw_attribute_data.lstrip(ATTRIBUTE_PREFIX)

        attribute_name, raw_params = prefixless_data.split("(")
        raw_params = raw_params.rstrip(")")

        params = [param.replace("\"", "") for param in raw_params.split(", ")]
        return ParsedAttribute(attribute_name, params)
