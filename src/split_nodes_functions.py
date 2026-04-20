from textnode import *
from regex_extract_functions import *

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    node_results = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_results.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid markdown syntax")
        node_split = node.text.split(delimiter)
        for i in range(0, len(node_split)):
            if i % 2 != 0:
                node_results.append(TextNode(node_split[i], text_type))
            elif node_split[i] != "":
                node_results.append(TextNode(node_split[i], TextType.TEXT))
    return node_results

def split_nodes_image(old_nodes:list[TextNode]) -> list[TextNode]:
    node_results = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_results.append(node)
            continue

        images = extract_markdown_images(node.text)
        if len(images) == 0:
            node_results.append(node)
            continue

        while len(images) != 0:
            image_text = f"![{images[0][0]}]({images[0][1]})"
            node_split = node.text.split(image_text, maxsplit= 1)
            if node_split[0] != "":
                node_results.append(TextNode(node_split[0], TextType.TEXT))
            node_results.append(TextNode(images[0][0], TextType.IMAGE, images[0][1]))
            images.remove(images[0])
            node.text = node_split[1]

        if node.text != "":
            node_results.append(TextNode(node.text, TextType.TEXT))

    return node_results 
        

def split_nodes_link(old_nodes:list[TextNode]) -> list[TextNode]:
    node_results = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_results.append(node)
            continue

        links = extract_markdown_links(node.text)
        if len(links) == 0:
            node_results.append(node)
            continue

        while len(links) != 0:
            link_text = f"[{links[0][0]}]({links[0][1]})"
            node_split = node.text.split(link_text, maxsplit= 1)
            if node_split[0] != "":
                node_results.append(TextNode(node_split[0], TextType.TEXT))
            node_results.append(TextNode(links[0][0], TextType.LINK, links[0][1]))
            links.remove(links[0])
            node.text = node_split[1]

        if node.text != "":
            node_results.append(TextNode(node.text, TextType.TEXT))

    return node_results 