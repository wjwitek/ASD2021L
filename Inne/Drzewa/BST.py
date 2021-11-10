class Node:
    def __init__(self, value):
        self.val = value
        self.parent = None
        self.left = None
        self.right = None
        self.misc = None  # any additional info needed for specific problem


class Tree:
    def __init__(self):
        self.root = None

    def in_order_walk(self, node):
        if node is not None:
            self.in_order_walk(node.left)
            print(node.val, end=" ")
            self.in_order_walk(node.right)
            if node == self.root:
                print()

    def in_order_array(self, node, result):
        if node is not None:
            self.in_order_array(node.left, result)
            result.append(node.val)
            self.in_order_array(node.right, result)
            if node == self.root:
                return result

    def find_key(self, key):
        node = self.root
        while node is not None and node.val != key:
            if node.val > key:
                node = node.left
            elif node.val < key:
                node = node.right
        return node

    @staticmethod
    def minimum(node):
        while node.left is not None:
            node = node.left
        return node

    @staticmethod
    def maximum(node):
        while node.right is not None:
            node = node.right
        return node

    def successor(self, node):
        if node.right is not None:
            return self.minimum(node.right)
        prev = node
        node = node.parent
        while node is not None and prev == node.right:
            prev = node
            node = node.parent
        return node

    def predecessor(self, node):
        if node.left is not None:
            return self.maximum(node.left)
        prev = node
        node = node.parent
        while node is not None and prev == node.left:
            prev = node
            node = node.parent
        return node

    def insert(self, new_key, misc=None):
        new_node = Node(new_key)
        new_node.misc = None
        if self.root is None:
            self.root = new_node
            return True
        root = self.root
        prev = None
        while root is not None:
            prev = root
            if new_key < root.val:
                root = root.left
            elif new_key == root.val:
                return False
            else:
                root = root.right
        new_node.parent = prev
        if new_key < prev.val:
            prev.left = new_node
        else:
            prev.right = new_node
        return True

    def delete_one_child(self, node):
        if node == self.root:
            if node.right == node.left is None:
                self.root = None
            elif node.right is None:
                node.left.parent = None
                self.root = node.left
            else:
                node.right.parent = None
                self.root = node.right
        else:
            if node.left == node.right is None:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            elif node.left is None:
                if node.parent.left == node:
                    node.parent.left = node.right
                    node.right.parent = node.parent
                else:
                    node.parent.right = node.right
                    node.right.parent = node.parent
            else:
                if node.parent.left == node:
                    node.parent.left = node.left
                    node.left.parent = node.parent

    def remove(self, key):
        node = self.find_key(key)
        if node is None:
            return False
        if node.left is None or node.right is None:
            self.delete_one_child(node)
        else:
            substitute = self.successor(node)
            self.delete_one_child(substitute)
            if node != self.root:
                if node.parent.left == node:
                    node.parent.left = substitute
                else:
                    node.parent.right = substitute
                substitute.left = node.left
                substitute.right = node.right
                substitute.parent = node.parent
            else:
                substitute.left = node.left
                substitute.right = node.right
                substitute.parent = None
                self.root = substitute


test_tree = Tree()
test_tree.insert(5)
test_tree.insert(6)
test_tree.insert(4)
test_tree.insert(2)
test_tree.insert(3)
test_tree.insert(1)
test_tree.in_order_walk(test_tree.root)
test_tree.remove(5)
test_tree.in_order_walk(test_tree.root)
print(test_tree.root.val)
