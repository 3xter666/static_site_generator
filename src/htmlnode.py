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
class LeafNode(HTMLNode):
    def __init__(self, tag, value: str, props: Optional[dict] = None):
        super().__init__(tag=tag, value=value, props=props)
    def to_html(self):
        if self.text is None:
            raise ValueError("LeafNode must have a value")
        elif not self.tag:
            return self.text
        return f"<{self.tag} {self.props_to_html()}>{self.text}</{self.tag}>" if self.props is not None else f"<{self.tag}>{self.text}</{self.tag}>"
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: Optional[dict] = None):
        super().__init__(tag=tag, children=children, props=props,value = None)
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        elif not self.children:
            raise ValueError("ParentNode must have children")
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag} {self.props_to_html()}>{children_html}</{self.tag}>" if self.props is not None else f"<{self.tag}>{children_html}</{self.tag}>"