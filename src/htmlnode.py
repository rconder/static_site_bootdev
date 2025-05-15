class HtmlNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def __repr__(self) -> str:
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props.items()})"

    def to_html(self):
        raise Exception("Not Implemented")

    def props_to_html(self):
        result = ""
        for key,value in self.props.items():
            result += f"{key}=\"{value}\" "
        return result[:-1]
