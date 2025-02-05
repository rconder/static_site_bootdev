from textnode import * 

def split_nodes_delimiter(old_nodes,delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_node =[]
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception( 'Delimiter is missing')
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_node.append(TextNode(sections[i],TextType.TEXT))
            else:
                split_node.append(TextNode(sections[i],text_type))
        new_nodes.extend(split_node)
    return new_nodes
