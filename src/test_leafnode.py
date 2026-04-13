import unittest

from leafnode import *


class TestTextNode(unittest.TestCase):
    
    def test_LeafNode(self):
        node = LeafNode("p", "Hello, world!")
        noTag = LeafNode(None, "No Tag")
        withTagProps = LeafNode("a", "link text", {"href":"www.url.com"})
        withPropsNoTag = LeafNode(None, "link text", {"href":"www.url.com"})
        
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(noTag.to_html(), "No Tag")
        self.assertEqual(withTagProps.to_html(), "<a href=\"www.url.com\">link text</a>")
        self.assertEqual(withPropsNoTag.to_html(), "link text")


if __name__ == "__main__":
    unittest.main()