"""
f(i, j) - najmniejszy koszt bycia literą i w słowie W przez literę o indeksie j
Obliczam funkcję metodą bottom-up (tablica array), dla każdej litery w słowie W spośród wszystkich liter które według f
mogą być na tej pozycji rozważam wszystkie możliwe ich następniki i dla każdego następnika zapisuje minimalny koszt.
Na koniec biorę minimum z f(n, j).
Złożoność czasowa: O(L*L*W), gdzie L to liczba wierzchołków, a W to liczba liter w słowie
"""


from queue import Queue
from zad2testy import runtests


def let(ch): return ord(ch) - ord("a")


def letters(G, W):
    L, E = G
    n = len(L)
    m = len(W)
    # przekształcam G na listy sąsiedztwa + macierz z wagami
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    graph = [[] for _ in range(n)]
    for u, v, w in E:
        matrix[u][v] = matrix[v][u] = w
        graph[u].append(v)
        graph[v].append(u)
    array = [[-1 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        if L[i] == W[0]:
            array[0][i] = 0
    for i in range(m - 1):
        for j in range(n):
            if array[i][j] != -1:
                for u in graph[j]:
                    if L[u] == W[i + 1] and (array[i + 1][u] == -1 or array[i + 1][u] > array[i][j] + matrix[u][j]):
                        array[i + 1][u] = array[i][j] + matrix[u][j]
    minimum = -1
    for i in range(n):
        if array[m - 1][i] != -1 and (minimum == -1 or minimum > array[m - 1][i]):
            minimum = array[m - 1][i]
    return minimum


runtests(letters)


# to nieżej chyba działa, ale wydaje mi się, że ma niefajną złożoność
"""
Przekształcam graf na reprezentację macierzową, a następnie z każdego wierzchołka, który może być początkiem słowa
wykonuję BFS, ale bez zapisywania visited. Do kolejki przekazuje indeks wierzchołka i rolę której litery w słowie pełni.
Dodatkowo przechowuje tablicę (array), z wynikami funkcji f(i, j) = najmniejszy koszt bycią literą j słowa w przez
literę i, dzięki czemu nie przeglądam scieżek, które na pewno dałyby większy koszt.
Złożoność czasowa: ?  O(L*())
Złożoność pamięciowa: O(L^2 + L * W)
"""
"""
def letters(G, W):
    L, E = G
    n = len(L)
    m = len(W)
    array = [[-1 for _ in range(m)] for _ in range(n)]
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if L[i] == W[0]:
            array[i][0] = 0
    queue = Queue()
    # turn L, E into adjacency matrix
    for u, v, w in E:
        graph[u][v] = graph[v][u] = w
    for i in range(n):
        if L[i] == W[0]:
            queue.put((i, 0))
            while not queue.empty():
                u, idx = queue.get()
                if idx == m - 1:
                    continue
                for j in range(n):
                    if graph[u][j] != 0 and L[j] == W[idx + 1]:
                        if array[j][idx + 1] == -1 or array[j][idx + 1] > array[u][idx] + graph[u][j]:
                            array[j][idx + 1] = array[u][idx] + graph[u][j]
                            queue.put((j, idx + 1))
    minimum = float('inf')
    for i in range(n):
        if array[i][m - 1] != -1 and array[i][m - 1] < minimum:
            minimum = array[i][m - 1]
    return minimum
"""
