class HtmlNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def __repr__(self) -> str:
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise Exception("Not Implemented")
        return ""

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

class LeafNode(HtmlNode):
    def __init__(self,tag, value , props = None ):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props = None  ):
        super().__init__(tag,None,children,props)
    def to_html(self):
        if not self.tag:
            raise ValueError("All parents must have a tag")
        if not self.children:
            raise ValueError("All parents must have children")
        result = ""
        for child in self.children:
            result += f"{child.to_html()}"
        return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'
