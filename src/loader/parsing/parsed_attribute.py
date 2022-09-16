from dataclasses import dataclass
from typing import List


@dataclass
class ParsedAttribute:
    attribute_name: str
    parameters: List[str]
