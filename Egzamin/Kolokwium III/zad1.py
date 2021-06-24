"""
Dla każdego węzła zapisuje jak daleko jest na lewo (liczby ujemne) lub prawo (liczby dodatnie) od osi przechodzącej
przez root i rekurencyjnie rozważam w ten sposób wszystkie węzły. Kiedy wchodzę do węzła dodaję jego wartość do pozycji
albo w tablicy węzłów na lewo, albo węzłów na prawo, przedłużając tablicę jeśli zachodzi taka potrzeba.
Złożoność czasowa: O(n) - n to przejśćie, po węzłach, przejście po left i right zajmie maks n, bo nie mogą  być te
tablice dłuższe od liczby węzłów
"""


class Node:
    def __init__(self,key,left=None,right=None):
        self.key = key
        self.right = right
        self.left = left
        self.how_far = None


def resolve(node, left, right):
    if node.how_far > 0:
        if len(right) <= node.how_far:
            right.append(0)
        right[node.how_far] += node.key
    elif node.how_far == 0:
        if len(right) <= node.how_far:
            right.append(0)
        if len(left) <= node.how_far:
            left.append(0)
        left[0] += node.key
        right[0] += node.key
    else:
        temp = abs(node.how_far)
        if len(left) <= temp:
            left.append(0)
        left[temp] += node.key

    if node.right is not None:
        node.right.how_far = node.how_far + 1
        resolve(node.right, left, right)
    if node.left is not None:
        node.left.how_far = node.how_far - 1
        resolve(node.left, left, right)


def maxi_suma_pionowa(root):
    left = []
    right = []
    current_maximum = -float('inf')
    current_minimum = float('inf')
    root.how_far = 0
    resolve(root, left, right)
    for num in left:
        if num > current_maximum:
            current_maximum = num
        if num < current_minimum:
            current_minimum = num
    for num in right:
        if num > current_maximum:
            current_maximum = num
        if num < current_minimum:
            current_minimum = num
    return current_maximum, current_minimum



root = Node(1)
root.left = Node(2)
root.right = Node(3,Node(5,Node(7),Node(8)),Node(6))
print(maxi_suma_pionowa(root),"?=?",11,",",6)

root = Node(-10,
        Node(-20,
            None,
            Node(-11)),
        Node(100,
            Node(90,
                Node(5,
                    None,
                    Node(50)),
                Node(95)),
            Node(105,
                Node(102),
                None)))
print(maxi_suma_pionowa(root),"?=?",297,",",-15)
