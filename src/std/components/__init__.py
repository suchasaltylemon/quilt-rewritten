from .label import Label

_tag_map = {
    "label": Label
}


def get_component_from_tag_name(tag_name: str):
    return _tag_map.get(tag_name, None)
