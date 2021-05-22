class Node:
    def __init__(self, color=None, value=None):
        self.color = color
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.nil = None

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent

