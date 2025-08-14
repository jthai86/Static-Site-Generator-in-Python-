from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter
from split_nodes_media import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    """
    Converts raw markdown text into a list of TextNode objects, handling:
    - inline code (`code`)
    - bold (**bold**)
    - italic (_italic_)
    - images (![alt](url))
    - links ([text](url))
    """
    # Start with a single TextNode of type TEXT
    nodes = [TextNode(text, TextType.TEXT)]

    # Apply code split first
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    # Apply bold split
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    # Apply italic split
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    # Apply image split
    nodes = split_nodes_image(nodes)

    # Apply link split
    nodes = split_nodes_link(nodes)

    return nodes
