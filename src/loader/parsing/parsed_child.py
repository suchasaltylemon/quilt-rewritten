from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class ParsedChild:
    tag_name: str
    tag_attributes: Dict[str, str]
    children: List["ParsedChild"]
    tag_class: Optional[str] = None
