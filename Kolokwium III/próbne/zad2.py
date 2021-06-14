"""
Algorytm bardzo podobny do scalania posortowanych list - przechodzę drzewa in-order, trzymam tablicę aktualnie
rozważanych węzłów dla każdego węzła, minimum dodaje do nowego drzewa. Wynikowe drzewo będzie bardzo niezbalansowane,
więc można insert sprowadzić do dodawania dziecka do ostatniego z prawewj liścia w czasie O(1).
Złożoność czasowa: O(n^2k), gdzie n to liczba węzłów największego drzewa, bo w k drzewach dla n węzłów szukamy następnika
"""


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.last_right = root

    def insert(self, key):
        new_node = BSTNode(key)
        if self.root is None:
            self.root = new_node
            return True
        root = self.root
        while new_node.parent is None:
            if root.val < key:
                if root.right is None:
                    root.right = new_node
                    new_node.parent = root
                else:
                    root = root.right
            elif root.val == key:
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

    def add_right(self, new_node):
        if self.root is None:
            self.root = BSTNode(new_node)
            self.last_right = self.root
        elif self.last_right.val != new_node:
            self.last_right.right = BSTNode(new_node)
            self.last_right = self.last_right.right


class BSTNode:
    def __init__(self, val=0):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        # mozna dopisywac itp itd


def get_next(node):
    if node.right is not None:
        node = node.right
        while node.left is not None:
            node = node.left
        return node
    par = node.parent
    while par is not None and node == par.right:
        node = par
        par = par.parent
    return par


def in_order_tree_walk(root):
    if root is not None:
        in_order_tree_walk(root.left)
        print(root.val, end=" ")
        in_order_tree_walk(root.right)


def drzewa_jakies(tab) -> Tree:
    k = len(tab)
    nodes = [tab[i].root for i in range(k)]
    # find most left nodes
    for i in range(k):
        while nodes[i].left is not None:
            nodes[i] = nodes[i].left
    new_tree = Tree()
    # add nodes to new_tree
    all_none = False
    while not all_none:
        minimal = None
        all_none = True
        # find minimum node
        for i in range(k):
            if nodes[i] is not None:
                all_none = False
                if minimal is None or minimal.val > nodes[i].val:
                    minimal = nodes[i]
        # add minimum node to tree
        if minimal is not None:
            new_tree.add_right(minimal.val)
        # move minimum and those equal to minimum
        for i in range(k):
            if nodes[i] is not None and nodes[i].val == minimal.val:
                nodes[i] = get_next(nodes[i])
    return new_tree


if __name__ == "__main__":
    from zad2testy import runtests
    runtests(drzewa_jakies)
