import unittest

from textnode import *
from node_conversion_functions import *


class TestTextNode_to_HTMLNode(unittest.TestCase):
    def test_TextNode_to_HTMLNode(self):
        textNode = TextNode("Test text", TextType.TEXT)
        boldNode = TextNode("Test bold", TextType.BOLD)
        italicNode = TextNode("Test italic", TextType.ITALIC)
        codeNode = TextNode("Test code", TextType.CODE)
        linkNode = TextNode("Test link", TextType.LINK, "www.alink.com")
        imageNode = TextNode("Test image", TextType.IMAGE, "www.animage.com")

        self.assertEqual(textnode_to_htmlnode(textNode).to_html(), "Test text")
        self.assertEqual(textnode_to_htmlnode(boldNode).to_html(), "<b>Test bold</b>")
        self.assertEqual(textnode_to_htmlnode(italicNode).to_html(), "<i>Test italic</i>")
        self.assertEqual(textnode_to_htmlnode(codeNode).to_html(), "<code>Test code</code>")
        self.assertEqual(textnode_to_htmlnode(linkNode).to_html(), "<a href=\"www.alink.com\">Test link</a>")
        self.assertEqual(textnode_to_htmlnode(imageNode).to_html(), "<img src=\"www.animage.com\" alt=\"Test image\"></img>")

class TestText_to_TextNode(unittest.TestCase):
    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        solution = [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                ]
        self.assertListEqual(solution, text_to_textnode(text))

if __name__ == "__main__":
    unittest.main()