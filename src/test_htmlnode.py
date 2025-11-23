import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello World!", None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(), ' class="greeting" href="https://boot.dev"')
    
    def test_props_none(self):
        node = HTMLNode("p", "This is some text", None, None)
        self.assertEqual("", node.props_to_html())
        
    def test_props_none(self):
        node = HTMLNode("p", "This is some text", None, {})
        self.assertEqual("", node.props_to_html()) 
        
    def test_values(self):
        node = HTMLNode("div", "This is some text")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is some text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
    def test_repr(self):
        node = HTMLNode("p", "This is some text", None, {"href": "https://www.google.com"})
        self.assertEqual(node.__repr__(), "HTMLNode(p, This is some text, children: None, {'href': 'https://www.google.com'})")
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "This is a link", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">This is a link</a>')
        
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
if __name__ == "__main__":
    unittest.main()