# Weronika Witek
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif root.key < key:
            root = root.right
        else:
            root = root.left
    return None


def maximum(root):
    if root is None:
        return None
    while root.right is not None:
        root = root.right
    return root


def predecessor(root):
    if root.left is not None:
        return maximum(root.left)
    prev = root
    root = root.parent
    while root is not None:
        if prev is root.right:
            break
        prev = root
        root = root.parent
    return root


def insert(root, key):
    new_node = BSTNode(key)
    while new_node.parent is None:
        if root.key < key:
            if root.right is None:
                root.right = new_node
                new_node.parent = root
            else:
                root = root.right
        elif root.key == key:
            break
        else:
            if root.left is None:
                root.left = new_node
                new_node.parent = root
            else:
                root = root.left
    if new_node.parent is None:
        return False
    return True


def modify_parent_and_child(to_remove, new_child, root):
    if new_child is not None:
        new_child.parent = to_remove.parent
    if to_remove.parent is not None:
        if to_remove is to_remove.parent.right:
            to_remove.parent.right = new_child
        else:
            to_remove.parent.left = new_child
    # for changes to root to actually have an effect something like additional class BST
    # with self.root would be required
    else:
        root = new_child


def remove_node(root, to_remove):
    if to_remove.right == to_remove.left is None:
        modify_parent_and_child(to_remove, None, root)
    elif to_remove.right is None:
        modify_parent_and_child(to_remove, to_remove.left, root)
    elif to_remove.left is None:
        modify_parent_and_child(to_remove, to_remove.right, root)
    else:
        exchange = predecessor(to_remove)
        to_remove.key = exchange.key
        remove_node(root, exchange)


def remove(root, key):
    to_remove = find(root, key)
    if to_remove is None:
        return False
    remove_node(root, to_remove)
    return True


# function used for tests
# def in_order_tree_walk(root):
#     if root is not None:
#         in_order_tree_walk(root.left)
#         print(root.key, end=" ")
#         in_order_tree_walk(root.right)
