"""
W każdym węźle przechowuje sumę lewego poddrzewa i prawego poddrzewa, wartości te aktualizuję schodząc w dół przy
dodawaniu węzłów (najpierw sprawdzam, czy tego węzła już nie ma, żeby nie zrobić za dużych sum).
Kiedy chcę policzyć sumę to sumję to co mam w roocie (key, leftvalue i rightvalue), a natępnie odejmuje za duże
poddrzewa schodząc do jakiegoś liśćia, w ten sposób, że jak aktualny key jest mniejszy od y, to idę w prawo i
dalej szukam za dużych poddrzew, jak jest większy to odejmuje key, rightvalue i schodzę w lewo, bo moze być tam jeszcze
za duże poddrzewo, a jak jest równy to odejmuje prawe poddrzewo i już nie muszę szukać w lewym poddrzewie, bo
tam wszystkie wartośći będą mniejsze od y. Analogicznie odejmuję za małe poddrzewa.
Ponieważ jest to przejście ścieżką do liścia, to przy założeniu, że drzewo jest zbalansowane złożoność czasowa sumy
wynosi O(logn).
"""


class bst_node:
    def __init__(self,key,left=None,right=None):
        self.key = key
        self.left = left
        self.right = right
        self.left_value = 0
        self.right_value = 0  # to by mogła być jedna wartość i wtedy lewo podrzewo to, to co mam w lewym dziecku
        # ale tak mi łatwiej i czytelniej po prostu

    def __str__(self):
        ret = ""
        if self.left:
            ret += str(self.left) + "<"
        ret += str(self.key)
        if self.right:
            ret += "<" + str(self.right)
        return ret


def find(root, key):
    node = root
    while node is not None and node.key != key:
        if node.key > key:
            node = node.left
        elif node.key < key:
            node = node.right
    return node


def insert(root, key) -> bst_node:
    check = find(root, key)
    if check is not None:
        return root
    new_node = bst_node(key)
    if root is None:
        root = new_node
        return root
    r = root
    prev = None
    while r is not None:
        prev = r
        if key < r.key:
            r.left_value += key
            r = r.left
        elif key == r.key:
            return root
        else:
            r.right_value += key
            r = r.right
    if key < prev.key:
        prev.left = new_node
    else:
        prev.right = new_node
    return root


def suma(T, x, y) -> float:
    result = T.key + T.left_value + T.right_value
    # odejmujemy za duże poddrzewa
    r = T
    while r is not None:
        if r.key < y:
            r = r.right
        elif r.key == y:
            result -= r.right_value
            break
        else:
            result -= r.right_value
            result -= r.key
            r = r.left
    # odejmujemy za małe poddrzewa
    r = T
    while r is not None:
        if r.key > x:
            r = r.left
        elif r.key == x:
            result -= r.left_value
            break
        else:
            result -= r.left_value
            result -= r.key
            r = r.right
    return result
















# testy:
T = [-1.0,-2.0,-1.1,10.0,9.0,9.5,0.5,10.5,10.2,5.0]
root = None
for elem in T:
    root = insert(root,elem)

print(suma(root,-2.0,-1.0),"?=?",-4.1)
root = insert(root,-1.5)
print(suma(root,-2.0,-1.0),"?=?",-5.6)

print(suma(root,5.0,9.5),"?=?",5.0 + 9.0 + 9.5)
root = insert(root,6.7)
print(suma(root,5.0,9.5),"?=?",5.0 + 9.0 + 9.5 + 6.7)
inf = float('inf')
print(suma(root,-inf,inf),"?=?",55.8)

