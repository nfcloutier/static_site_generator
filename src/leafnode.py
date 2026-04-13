from htmlnode import *
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("No value provided")
        if self.tag is None:
            return str(self.value)
        prepend = f"<{self.tag}{self.props_to_html()}>" if self.tag is not None else ""
        append = f"</{self.tag}>" if self.tag is not None else ""
        return f"{prepend}{self.value}{append}"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"