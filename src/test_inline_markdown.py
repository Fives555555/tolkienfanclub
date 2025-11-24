import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT), 
            TextNode("bold", TextType.BOLD), 
            TextNode(" word", TextType.TEXT)
        ])
        
    def test_delim_two_bold(self):
        node = TextNode("This is text with a **bold** word and **another**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD), 
            TextNode(" word and ", TextType.TEXT),
            TextNode("another", TextType.BOLD)
        ])

    def test_delim_muli_bold(self):
        node = TextNode("This is text with a **bold word** and **another**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold word", TextType.BOLD), 
            TextNode(" and ", TextType.TEXT),
            TextNode("another", TextType.BOLD)
        ])

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(new_nodes, [
            TextNode("This is text with an ", TextType.TEXT), 
            TextNode("italic", TextType.ITALIC), 
            TextNode(" word", TextType.TEXT)
        ])        

    def test_delim_bold_and_italic(self):
        node = TextNode("This is text with a **bold** word and an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD), 
            TextNode(" word and an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ])        

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` inside", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT), 
            TextNode("code block", TextType.CODE), 
            TextNode(" inside", TextType.TEXT)
        ])       

if __name__ == "__main__":
    unittest.main()