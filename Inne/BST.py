class TreeNode:
    def __init__(self, value=None):
        self.val = value
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def in_order_tree_walk(self, node=TreeNode('start')):
        if node.val == 'start':
            node = self.root
        if node is not None:
            self.in_order_tree_walk(node.left)
            print(node.val, end=" ")
            self.in_order_tree_walk(node.right)

    def tree_search(self, key, x=None):
        if x is None:
            x = self.root
        while x is not None and x.val != key:
            if x.val < key:
                x = x.right
            else:
                x = x.left
        return x

    def minimum(self, x=None):
        if x is None:
            x = self.root
        while x.left is not None:
            x = x.left
        return x

    def maximum(self, x=None):
        if x is None:
            x = self.root
        while x.right is not None:
            x = x.right
        return x

    def tree_successor(self, x):
        if x.right is not None:
            return self.minimum(x.right)
        y = x.p
        while y is not None and y.right is x:
            x = y
            y = y.p
        return y

    def tree_predecessor(self, x):
        if x.left is not None:
            return self.maximum(x.left)
        y = x.p
        while y is not None and y.left is x:
            x = y
            y = y.p
        return y

    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif y.val > z.val:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def tree_delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y is not z.right:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y


test_tree = BST()
test_tree.root = TreeNode(5)
tab = [6, 3, 7, 1, 4, 10]
for i in tab:
    test_tree.insert(TreeNode(i))
print(test_tree.root.left.val)
test_tree.in_order_tree_walk()
