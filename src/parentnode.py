from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag provided")
        if self.children is None or len(self.children) == 0:
            raise ValueError("No children provided")
        
        prepend = f"<{self.tag}{self.props_to_html()}>" if self.props is not None and len(self.props) != 0 else f"<{self.tag}>"
        append = f"</{self.tag}>"

        result = prepend
        for child in self.children:
            result += child.to_html()
        result += append

        return result