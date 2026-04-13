import unittest

from textnode import *
from textnode_to_htmlnode import *


class TestTextNode_to_HTMLNode(unittest.TestCase):
    def test_TextNode_to_HTMLNode(self):
        textNode = TextNode("Test text", TextType.TEXT)
        boldNode = TextNode("Test bold", TextType.BOLD)
        italicNode = TextNode("Test italic", TextType.ITALIC)
        codeNode = TextNode("Test code", TextType.CODE)
        linkNode = TextNode("Test link", TextType.LINK, "www.alink.com")
        imageNode = TextNode("Test image", TextType.IMAGE, "www.animage.com")

        self.assertEqual(text_node_to_html_node(textNode).to_html(), "Test text")
        self.assertEqual(text_node_to_html_node(boldNode).to_html(), "<b>Test bold</b>")
        self.assertEqual(text_node_to_html_node(italicNode).to_html(), "<i>Test italic</i>")
        self.assertEqual(text_node_to_html_node(codeNode).to_html(), "<code>Test code</code>")
        self.assertEqual(text_node_to_html_node(linkNode).to_html(), "<a href=\"www.alink.com\">Test link</a>")
        self.assertEqual(text_node_to_html_node(imageNode).to_html(), "<img src=\"www.animage.com\" alt=\"Test image\"></img>")


if __name__ == "__main__":
    unittest.main()