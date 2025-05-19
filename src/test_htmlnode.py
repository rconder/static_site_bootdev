import unittest

from htmlnode import HtmlNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_prop(self):
        node = HtmlNode(props={"href": "https://www.google.com","target": "_blank",})
        result = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(result,node.props_to_html())

    def test_prop2(self):
        node = HtmlNode(props={"href": "https://google.com","target": "_blank",})
        result = " href=\"https://google.com\" target=\"_blank\""
        self.assertEqual(result,node.props_to_html())

    def test_repr(self):
        props={"href": "https://google.com","target": "_blank",}
        node = HtmlNode(props=props)
        result = f"HtmlNode(None, None, None, {props})"
        self.assertEqual(result,node.__repr__())

    def test_values(self):
        node = HtmlNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr_2(self):
        node = HtmlNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HtmlNode(p, What a strange world, None, {'class': 'primary'})",
        )
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p2(self):
            node = LeafNode("p", "This is a paragraph of text.")
            self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_to_html_p3(self):
        node = LeafNode("a", "Click me!", props ={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

if __name__ == "__main__":
    unittest.main()
