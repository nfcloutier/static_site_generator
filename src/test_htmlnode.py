import unittest

from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        empty = HTMLNode()
        tagOnly = HTMLNode("A tag")
        valueOnly = HTMLNode(value="A value")
        childrenOnly = HTMLNode(children=[tagOnly, valueOnly])
        propsOnly = HTMLNode(props={"one":"one's value", "two":"two's value"})
        for item in [empty, tagOnly, valueOnly, childrenOnly, propsOnly]:
            print(item)
        print(f"empty: '{empty.props_to_html()}'")
        print(f"propsOnly: '{propsOnly.props_to_html()}'")


if __name__ == "__main__":
    unittest.main()