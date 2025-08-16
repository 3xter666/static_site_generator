import unittest

from htmlnode import HTMLNode
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