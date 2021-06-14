# implementation of red-black trees, https://www.programiz.com/dsa/red-black-tree
# założenie: unikalne wartośći kluczy
red = True
black = False


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        if node.color:
            color = "red"
        else:
            color = "black"
        print("[", node.val, ",", color, "]", end=" ")
        in_order_traversal(node.right)


class Node:
    def __init__(self, val, color):
        self.val = val
        self.parent = None
        self.right = None
        self.left = None
        self.color = color


class RBTree:
    def __init__(self):
        self.root = None

    def print_tree(self):
        in_order_traversal(self.root)

    def rotation_left(self, x, y):
        x.right = y.left
        y.left = x
        y.parent = x.parent
        x.parent = y
        if self.root == x:
            self.root = y

    def rotate_right(self, x, y):
        y.left = x.right
        x.right = y
        x.parent = y.parent
        y.parent = x
        if self.root == y:
            self.root = x

    def sibling(self, node):
        if node == self.root:
            return None
        if node == node.parent.left:
            return node.parent.right
        else:
            return node.parent.left

    def uncle(self, node):
        if node == self.root:
            return None
        return self.sibling(node.parent)

    def insert(self, new_val):
        if self.root is None:
            self.root = Node(new_val, black)
        # find parent
        parent = self.root
        right = False
        while parent is not None:
            if parent.val > new_val:
                if parent.left is None:
                    break
                parent = parent.left
            elif parent.val == new_val:
                return False
            else:
                if parent.right is None:
                    right = True
                    break
                parent = parent.right
        new_node = Node(new_val, red)
        new_node.parent = parent
        if right:
            parent.right = new_node
        else:
            parent.left = new_node


# test_tree = RBTree()
# test_tree.root = Node(10,black)
# node = Node(5, red)
# test_tree.root.left = node
# node_2 = Node(1, black)
# node.left = node_2
# node_2 = Node(6, black)
# node.right = node_2
# node = Node(14, red)
# test_tree.root.right = node
# node_2 = Node(12, black)
# node.left = node_2
# node_2 = Node(15, black)
# node.right = node_2
# test_tree.print_tree()
# test_tree.rotation_left(test_tree.root, test_tree.root.right)
# print(test_tree.root.val)
# test_tree.print_tree()

