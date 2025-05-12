import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node,node2)
    
    def test_repr_works(self):
      noderep = TextNode("This is a text node", TextType.BOLD).__repr__()
      self.assertEqual(noderep, "TextNode(This is a text node, bold, None)")
    
    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_equal_with_empty(self):     
        node = TextNode("", TextType.BOLD)
        node2 = TextNode("", TextType.BOLD)
        self.assertEqual(node,node2)
        
if __name__ == "__main__":
    unittest.main() 