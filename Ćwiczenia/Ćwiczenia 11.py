from collections import deque


# BST - predecessor and successor
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.misc = None  # for storing additional values, not required in BSTNode


def maximum(root):
    if root is None:
        return None
    while root.right is not None:
        root = root.right
    return root


def minimum(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
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


def successor(root):
    if root.right is not None:
        return minimum(root.right)
    prev = root
    root = root.parent
    while root is not None:
        if prev is root.left:
            break
        prev = root
        root = root.parent
    return root


# Finding maximum flow for multiple sources and destinations
"""
Create two additional nodes - main source and main destination. Main source will be connected to each of source with
edge that has infinite flow and similarly each destination will be connected with main destination. Then
Ford-Fulkerson algorithm can be used to determine maximum flow using main source and main destination.
"""


"""
Zad 1 z maksymalnego przepływu
Prosze wskazac algorytm, który znajduje
maksymalny przepływ miedzy zródłem i ujsciem w grafie nieskierowanym. Prosze uzyc algorytmu z
wykładu—dla grafów skierowanych, gdzie miedzy kazda para wierzchołków jest najwyzej jedna krawedz—
jako czarnej skrzynki. Alternatywnie mozna opisac implementacje bezposrednio pracujaca na grafie nieskierowanym.
Pomysły:
- zamiana na graf krawędziowy?
"""


"""
Zad 2 z maksymalnego przepływu
Dany jest graf nieskierowany G = (V,E). Mówimy, ze spójnosc
krawedziowa G wynosi k jesli usuniecie pewnych k krawedzi powoduje, ze G jest niespójny, ale usuniecie
dowolnych k − 1 krawedzi nie rozspójnia go. Prosze podac algorytm, który oblicza spójnosc krawedziowa
danego grafu.
Pomysł:
Wybiramy dowolny wierzchołek v i dla każdego możliwego ujścia wykonujemy algorytm Edemona-Karpa. Spośród otrzymanych
maksymalnych przepływów wybieramy minimum. Jest to szukana spójność krawędziowa grafu.
"""


"""
Zad 3 z maksymalnego przepływu
Dana jest formuła logiczna
postaci: C1 , C2 ,  , Cm, gdzie kazda Ci to klauzula bedaca alternatywa zmiennych i/lub ich zaprzeczen.
Wiadomo, ze kazda zmienna wystepuje w formule dokładnie dwa razy, raz zanegowana i raz niezanegowana.
Na przykład ponizsza formuła stanowi dopuszczalne wejscie:
(x - y - z) , (y - w) , (z - v) , (x - w) , (v).
Prosze podac algorytm, który oblicza takie wartosci zmiennych, ze formuła jest prawdziwa.
Pomysł:
Tworzymy graf z "sztucznym" źródłem z krawędziami o pojemności inf do wierchołków reprezentujących kolejne zmienne.
Z każdej zmiennej wychodzą po dwie krawędzi do zmienna i not zmienna, obie o pojemnośći 1. Następnie tworzymy
wierzchołki reprezentujące klauzule i do nich doprowadzamy krawędzie z literałów, które zawierają. Analogicznie do
źródła, z każdej klauzuli prowadzimy krawędź o pojemości inf do "sztucznego" ujśćia. Na koniec wykonujemy algorytm
Forda-Fulkersona. Jeśli wartość maksymalnego przepływu zgadza się z liczbą klazul, to formuła jest spełnialna.
"""


"""
Zad 4 z maksymalnego przepływu
Prosze podac algorytm, który majac na wejsciu drzewo oblicza
skojarzenie o maksymalnej licznosci. Czy algorytm dalej bedzie działac jesli kazda krawedz bedzie miec
dodatnia wage i szukamy skojarzenia o maksymalnej sumie wag?
Pomysł: Postępujemy bardzo podobnie do algorytmu rozwiązującego problem imprezy firmowej. Definujemy dwie funkcja:
f(x) - maksymalne skojarzenie w poddrzewie x
g(x) - maksymalne skojarzenie w poddrzewie x, jesli nie bierzemy żadenj z krawędzi od x do dzieci
Zapisując bardziej preczyjnie:
g(x) = suma po dzieciach z f(x)
f(x) = max(g(x), g(x)+max po dzieciach z g(d)-f(d)+1)
Rekurencyjnie szukamy f(root).
"""


def f(graph, f_val, x, g_val):
    if f_val[x] != -1:
        return f_val[x]
    result = g(graph, f_val, x, g_val)
    for child in graph[x]:
        temp = result - f(graph, f_val, child, g_val) + g(graph, f_val, child, g_val) + 1
        if temp > result:
            result = temp
    return result


def g(graph, f_val, x, g_val):
    if g_val[x] != -1:
        return g_val[x]
    result = 0
    for child in graph[x]:
        result += f(graph, f_val, child, g_val)
    return result


# for adjacency list, assumes root has index 0
def matching(tree):
    n = len(tree)
    f_val = [-1 for _ in range(n)]
    g_val = [-1 for _ in range(n)]
    return f(tree, f_val, 0, g_val)


"""
Zad 5 z maksymalnego przepływu
Dany jest graf skierowany G = (V,E) oraz wierzchołki s i t. Prosze
zaproponowac algorytm znajdujacy maksymalna liczbe rozłacznych (wierzchołkowo) sciezek miedzy s i t.
Pomysł:
Tworzymy graf krawędziowy i obliczamy maksymlalny przepływ z s do t ?
"""


"""
Zad 1 z BST
Rozwazmy drzewa BST, które dodatkowo w kazdym wezle
zawieraja pole z liczba wezłów w danym poddrzewie. Prosze opisac jak w takim drzewie wykonywac
nastepujace operacje:
1. znalezienie i-go co do wielkosci elementu,
2. wyznaczenie, którym co do wielkosci w drzewie jest zadany wezeł
Prosze zaimplementowac obie operacje.
Pomysł: 
a: Rekurencyjnie schodzimy w dół, przy czym schodząc w prawo zmniejszamy wartość i
b: Przechodzimy do roota i potem z powrotem schodząc tą samą scieżką obliczamy ile wezłów "zostawiamy" po lewej
"""


def find_element(root, i):
    if root.left is not None:
        if root.left.misc + 1 == i:
            return root
        elif root.left.misc >= i:
            find_element(root.left, i)
        elif root.right is not None:
            find_element(root.right, i - root.left.misc - 1)
        else:
            return None
    elif i == 1:
        return root


def find_element_value(node):
    queue = deque()
    counter = 1
    queue.append(node)
    while node.parent is not None:
        queue.append(node.parent)
        node = node.parent
    result = 0
    while counter > 0:
        node = queue.pop()
        if node.left is not None:
            result += node.left.misc
        result += 1
        counter -= 1
    return result - 1


"""
Zad 2 z BST
Prosze zapropnowac algorytm, który oblicza sume wszystkich wartosci w drzewie binarnym
zdefiniowanym na wezłach typu:
class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = val
Program moze korzystac wyłacznie ze stałej liczby zmiennych (ale wolno mu zmieniac strukture drzewa, pod
warunkiem, ze po zakonczonych obliczeniach drzewo zostanie przywrócone do stanu poczatkowego.)
Pomysł: zawsze schodzimy najbardziej w lewo jak się da, a dopiero potem w prawo, więc jak wracamy od prawej
strony to wiemy (czyli trzeba też przechowywać informację skąd przyszliśmy), że to co jest po lewej już jest w sumie.
Będą więc przypadki:
- poprzedni node to parent obencego: jeśli się da to idź do lewego dziecka, jak nie to do prawego, a jak jest to
liść, to dodaj jego wartość do sumy i idź do rodzica
- poprzedni node, to lewe dziecko obecnego: jeśli się da to idź do prawego dziecka, jak nie to dodaj jego wartość do
sumy i idź do rodzica
- poprzedni node, to prawe dziecko obecnego: dodaj jego wartość do sumy i idź do rodzica
- obecny node to none (parent root'a): zwróć sumę
Złożoność czasowa: O(n)
"""


def sum_of_tree(root):
    if root is None:
        return 0
    if root.left is not None:
        current = root.left
        prev = root
    elif root.right is not None:
        current = root.right
        prev = root
    else:
        return root.val
    result = 0
    while current is not None:
        if current.parent == prev:
            prev = current
            if current.left is not None:
                current = current.left
            elif current.right is not None:
                current = current.right
            else:
                result += current.key
                current = current.parent
        elif current.left == prev:
            prev = current
            if current.right is not None:
                current = current.right
            else:
                result += current.key
                current = current.parent
        else:
            result += current.key
            prev = current
            current = current.parent
    return result
