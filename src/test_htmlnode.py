import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props=None)
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_with_props(self):
        node = HTMLNode(tag="a", value="Click me", props={"href": "https://example.com", "target": "_blank"})
        self.assertIn('href="https://example.com"', node.props_to_html())
        self.assertIn('target="_blank"', node.props_to_html())
    
    def test_props_to_html_empty_props(self):
        node = HTMLNode(tag="p", value="Text", props={})
        self.assertEqual(node.props_to_html(), "")
    
    def test_repr_method(self):
        node = HTMLNode(tag="span", value="Text", props={"class": "highlight"})
        repr_result = repr(node)
        self.assertIn("tag=span", repr_result)
        self.assertIn("text=Text", repr_result)
        self.assertIn("class=\"highlight\"", repr_result)
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_span_with_props(self):
        node = LeafNode("a", "Important text", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Important text</a>")
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )