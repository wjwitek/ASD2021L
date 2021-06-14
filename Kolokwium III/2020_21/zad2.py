"""
Weronika Witek
założenie: nie można usuwać liści i korzenia
f(i) = najmniejsza możliwa suma wierzchołków oddzielającyh dla poddrzewa o korzeniu w węźle i
f(i) = min{f(i.left)+f(i.right), i.value}  (przy czym dla liści f(i) = inf)
Rozwiązaniem jest f(T), które obliczam w ten sposób, że zawsze jeśli mogę to schodzę w dół w lewo, zachowując
jednocześnie skąd przyśliśmy:
- jeśli z rodzica, to idziemy do kolejnego dziecka, jak to liść to wrcam do rodzica
- jeśli z lewego dziecka to idę do prawego dziecka
- jeśli z lewego dziecka to rozważam min (podmieniam wartości value na f(i), zakładam, że jeśli w poleceniu nie ma nic
o tym, że drzewo ma zahchować swoją postać, to mogę je zmieniać, jeśli jest to problem, to nizej w komentarzu mam też
rozwiązanie rekurencyjne, które nie zmienia drzewa)
Złożoność: O(n) - każdy wierzchołek odwiedzamy co najwyżej dwa razy
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


"""
# rozwiązanie rekurencyjne, nie niszczy drzewa, ale zajmuje więcej pamięci:
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
"""


def f(node):
    if is_leaf(node):
        node.value = float('inf')
    elif node.right is None:
        node.value = min(node.value, node.left.value)
    elif node.left is None:
        node.value = min(node.value, node.right.value)
    else:
        node.value = min(node.value, node.right.value + node.left.value)


def cutthetree(T):
    prev = None
    current = T
    while current is not None:
        if prev == current.parent:
            prev = current
            if current.left is not None:
                current = current.left
            elif current.right is not None:
                current = current.right
            else:
                f(current)
                current = current.parent
        elif prev == current.left:
            prev = current
            if current.right is not None:
                current = current.right
            else:
                f(current)
                current = current.parent
        elif prev == current.right:
            f(current)
            prev = current
            current = current.parent
    return T.left.value + T.right.value


    
runtests(cutthetree)


