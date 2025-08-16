from typing import Optional

class HTMLNode:
    def __init__(self, tag: Optional[str] = None, value: Optional[str] = None, children: Optional[list] = None, props: Optional[dict] = None):
        self.tag = tag
        self.text = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    def props_to_html(self):
        if not self.props:
            return ""
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())
    def __repr__(self):
        props = self.props_to_html()
        return f"HTMLNode(tag={self.tag}, text={self.text}, children={self.children}, props={props})"
