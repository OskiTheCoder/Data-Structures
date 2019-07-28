"""
Binary Search Tree that supports insert and find.

2017
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:

    def _init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_node(self, self.root, value)

    def insert_node(self, root, value):
        if root.val > value:
            left_node = root.left
            if left_node:
                self.insert_node(root.left,value)
            else:
                root.left = Node(value)
                return root
        else:
            right_node = root.right
            if right_node:
                self.insert_node(root.right, value)
            else:
                root.right = Node(value)
                return root

    def find(self, value):
        return self.find(self.root, value)

    def find_node(self, root, value):
        if not root:
            return False
        if root.val == value:
            return True
        if root.val > value:
            return self.insert_node(root.left, value)
        else:
            return self.insert_node(root.right, value)







