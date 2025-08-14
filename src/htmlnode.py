from typing import Optional

class HTMLNode:
    def __init__(self, tag: str, value : str, children : list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
