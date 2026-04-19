from textnode import *

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    node_results = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_results.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid markdown syntax")
        node_split = node.text.split(delimiter)
        print(node_split)
        for i in range(0, len(node_split)):
            if i % 2 != 0:
                node_results.append(TextNode(node_split[i], text_type))
            elif node_split[i] != "":
                node_results.append(TextNode(node_split[i], TextType.TEXT))
    return node_results