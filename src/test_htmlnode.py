import unittest

from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_HTMLNode(self):
        empty = HTMLNode()
        tagOnly = HTMLNode("A tag")
        valueOnly = HTMLNode(value="A value")
        childrenOnly = HTMLNode(children=[tagOnly, valueOnly])
        propsOnly = HTMLNode(props={"one":"one's value", "two":"two's value"})

        self.assertEqual(repr(empty), "HTMLNode(None, None, None, None)")
        self.assertEqual(repr(tagOnly), "HTMLNode(A tag, None, None, None)")
        self.assertEqual(repr(valueOnly), "HTMLNode(None, A value, None, None)")
        self.assertEqual(repr(childrenOnly), "HTMLNode(None, None, [HTMLNode(A tag, None, None, None), HTMLNode(None, A value, None, None)], None)")
        self.assertEqual(repr(propsOnly), "HTMLNode(None, None, None, {'one': \"one's value\", 'two': \"two's value\"})")
        
        self.assertEqual(empty.props_to_html(), "")
        self.assertEqual(propsOnly.props_to_html(), " one=\"one's value\" two=\"two's value\"")

if __name__ == "__main__":
    unittest.main()