from classes import Node, Stack
import unittest
#
# class TestStack(unittest.TestCase):
#     def setUp(self) -> None:
#         self.stack = Stack()
#
#     def

class TestStack(unittest.TestCase):
    def test_Node(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
        stack.push('data')
        self.assertEqual(stack.top.data, 'data')