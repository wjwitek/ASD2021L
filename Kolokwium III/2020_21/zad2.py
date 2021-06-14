"""
Weronika Witek
założenie: nie można usuwać liści i korzenia
f(i) = najmniejsza możliwa suma wierzchołków oddzielającyh dla poddrzewa o korzeniu w węźle i
f(i) = min{f(i.left)+f(i.right), i.value}  (przy czym dla liści f(i) = inf)
Rozwiązaniem jest f(T), które obliczam rekurencyjnie (nie ma potzeby spamiętywania wyników, bo dla każdego i, f(i)
będzie wywołane co najwyżej raz - przez jego rodzica)
Złożoność: O(n) - każdy wierzchołek odwiedzamy co najwyżej raz
"""
from zad2testy import runtests


class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def is_leaf(node):
    if node.left == node.right is None:
        return True
    return False


def smallest_sum(T, node):
    if node == T:  # dla korzenia nie rozważamy min, bo nie można go usunąć
        return smallest_sum(T, node.right) + smallest_sum(T, node.left)
    # nie rozważam node.left == node.right is None, bo funkcja nie powinna dojść do węzła, który jest liściem
    if (node.left is None and is_leaf(node.right)) or (node.right is None and is_leaf(node.left)):
        return node.value
    elif node.left is None:
        return min(smallest_sum(T, node.right), node.value)
    elif node.right is None:
        return min(smallest_sum(T, node.left), node.value)
    elif is_leaf(node.left) or is_leaf(node.right):  # musimy wziąć value węzła jeśli któreś z jego dzieci jest liściem
        return node.value
    return min(smallest_sum(T, node.right) + smallest_sum(T, node.left), node.value)


def cutthetree(T):
    return smallest_sum(T, T)

    
runtests(cutthetree)


