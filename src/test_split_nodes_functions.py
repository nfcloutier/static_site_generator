'''old_nodes = [
    TextNode("**This is _text_ with a `code block` word**", TextType.TEXT),
    TextNode("`This is` text with a code block word", TextType.TEXT),
    TextNode("This is text with a code block `word`", TextType.TEXT),
    TextNode("`This is`` text with` a `code block` `word`", TextType.TEXT),
]

delimiter = "`"

text_type = TextType.CODE

for node in split_nodes_delimiter(old_nodes, delimiter, text_type):
    print(node)
'''
import unittest

from split_nodes_functions import *
from textnode import *


class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_plain_text(self):
        test_node = TextNode("This is just plain text", TextType.TEXT)
        self.assertListEqual(split_nodes_delimiter([test_node], "_", TextType.ITALIC), [TextNode("This is just plain text", TextType.TEXT)])
    
    def test_not_text(self):
        test_node = TextNode("This is a non text block", TextType.CODE)
        self.assertListEqual(split_nodes_delimiter([test_node], "`", TextType.CODE), [test_node])
    
    def test_missing_delimiter(self):
        test_node = TextNode("This is a _strange_ _amount", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [test_node], "_", TextType.ITALIC)

    def test_one_instance(self):
        test_node = TextNode("This has **bold text** in it", TextType.TEXT)
        self.assertListEqual(split_nodes_delimiter([test_node], "**", TextType.BOLD), [TextNode("This has ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode(" in it", TextType.TEXT)])

    def test_multiple_instance(self):
        test_node = TextNode("This has italic _here_ but also _here_", TextType.TEXT)
        self.assertListEqual(split_nodes_delimiter([test_node], "_", TextType.ITALIC), [TextNode("This has italic ", TextType.TEXT), TextNode("here", TextType.ITALIC), TextNode(" but also ", TextType.TEXT), TextNode("here", TextType.ITALIC)])

    def test_multiple_multitype_instance(self):
        test_node = TextNode("This has **bold** and `code`", TextType.TEXT)
        result1 = split_nodes_delimiter([test_node], "`", TextType.CODE)
        self.assertListEqual(result1, [TextNode("This has **bold** and ", TextType.TEXT), TextNode("code", TextType.CODE)])
        self.assertListEqual(split_nodes_delimiter(result1, "**", TextType.BOLD), [TextNode("This has ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" and ", TextType.TEXT), TextNode("code", TextType.CODE)])

class TestSplitNodesImagesAndLinks(unittest.TestCase):

    def test_split_nodes_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_nodes_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()