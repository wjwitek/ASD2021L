"""
f(i) - suma najlepszego podrzewa, dla którego węzeł i jest początkiem (plus liczba krawędzi jakie zawiera), tzn.
wszystkie pozostałe krawędzi są niżej w drzewie
f(i) szukam w ten sposób, że "dodaje" krawędzie do dzieci i poddrzewa dzieci, najmniejsze poddrzewa w podrzewie, aż nie
mam k krawędzi
Złożoność czasowa: O(nk^2)
Złożoność pamięciowa: O(n)

Lepsze rozwiązanie Lukasza: dynamik, w każdym wierzchołku rozważamy każdą możliwą liczbę krawędzi drzewa kończącego sie
w danym wierzchołku.
"""
from zad2testy import runtests


class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.leftval = 0     # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None  # prawe poddrzewo
        self.rightval= 0     # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane
        self.parent = None  # nie wiem czy mogę dołożyć, ale zawsze mogłoby to być wew. X,
        # nie chce mi się po prostu kodu przerabiać


def find_smallest(node, to_del):
    if node is None:
        return
    smallest = float('inf')
    smallest_node = None
    if node.left is not None and node.left.X is not None:
        r = node.left
    else:
        r = node.right
    prev = node
    while r is not node.parent:
        if r.left is not None and r.left.X is not None and r.left.X[0] + r.leftval < smallest and r.left.X[1] + 1 <= to_del:
            smallest = r.left.X[0] + r.leftval
            smallest_node = r.left
        if r.right is not None and r.right.X is not None and r.right.X[0] + r.rightval < smallest and r.right.X[1] + 1 <= to_del:
            smallest = r.right.X[0] + r.rightval
            smallest_node = r.right
        if r.parent is prev and r.left is not None and r.left.X is not None:
            prev = r
            r = r.left
        elif r.parent is prev and r.right is not None and r.right.X is not None:
            prev = r
            r = r.right
        else:
            prev = r
            r = r.parent
    smallest_k = smallest_node.X[1] + 1
    smallest_node.X = None
    r = smallest_node.parent
    while r is not node.parent:
        r.X = (r.X[0] - smallest, r.X[1] - smallest_k)
        r = r.parent


def valuableTree(T, k):
    best_value = -float('inf')

    def calc(node, max_k):
        nonlocal best_value
        value, k = 0, 0
        if node.left is not None:
            node.left.parent = node
            if node.left.X is None:
                calc(node.left, max_k)
            value += node.left.X[0] + node.leftval
            k += node.left.X[1] + 1
        if node.right is not None:
            node.right.parent = node
            if node.right.X is None:
                calc(node.right, max_k)
            value += node.right.X[0] + node.rightval
            k += node.right.X[1] + 1
        if k + 2 <= max_k:
            node.X = (value, k)
        else:
            node.X = (value, k)
            while node.X[1] > max_k:
                find_smallest(node, node.X[1] - max_k)
        if node.X[1] == max_k and best_value < node.X[0]:
            best_value = node.X[0]

    calc(T, k)

    return best_value


runtests(valuableTree)


