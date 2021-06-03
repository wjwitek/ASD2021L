from queue import PriorityQueue
from math import log2


# implementation of family of disjoint sets
class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


# implementation of Kruskal algorithm for list of edges
def kruskal_edges(edges, n):
    # edges is a list ot tuples: (u, v, w({u, v}))
    # n - number of vertices in graph (can be calculated in O(E))
    edges.sort(key=lambda x: x[2])
    vertices = [Node(i) for i in range(n)]
    result = []
    for u, v, w in edges:
        if find(vertices[u]) != find(vertices[v]):
            result.append((u, v))
            union(vertices[u], vertices[v])
    return result


kruskal_test = [(0, 1, 7), (0, 2, 1), (1, 2, 8), (1, 3, 3), (1, 5, 2), (4, 5, 5), (4, 3, 6), (2, 3, 12), (2, 4, 4)]
num = 6
print(kruskal_edges(kruskal_test, num))  # answer: [(0, 2), (1, 5), (4, 5), (2, 4), (1, 3)]


# implementation of Dijkstra algorithm for adjacency matrix
def dijkstra_matrix(graph, source):
    n = len(graph)
    shortest = [float('inf') for _ in range(n)]
    shortest[source] = 0
    queue = PriorityQueue()
    queue.put((0, source))
    while not queue.empty():
        p, u = queue.get()
        if p > shortest[u]:
            continue
        for i in range(n):
            if graph[u][i] != 0 and shortest[i] > shortest[u] + graph[u][i]:
                shortest[i] = shortest[u] + graph[u][i]
                queue.put((shortest[i], i))
    return shortest


dijkstra_matrix_test = [[0, 2, 1, 0, 0, 0, 0, 0], [2, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 3, 3, 1, 0, 0], [0, 1, 3, 0, 3, 0,
        0, 0], [0, 0, 3, 4, 0, 2, 0, 3], [0, 0, 1, 0, 2, 0, 2, 1], [0, 0, 0, 0, 0, 2, 0, 3], [0, 0, 0, 0, 3, 1, 3, 0]]
# correct: [0, 2, 1, 3, 4, 2, 4, 3]
print(dijkstra_matrix(dijkstra_matrix_test, 0))


def dijkstra_list(graph, source):
    n = len(graph)
    shortest = [float('inf') for _ in range(n)]
    shortest[source] = 0
    queue = PriorityQueue()
    queue.put((0, source))
    while not queue.empty():
        p, u = queue.get()
        if p > shortest[u]:
            continue
        for v, w in graph[u]:
            if shortest[v] > shortest[u] + w:
                shortest[v] = shortest[u] + w
                queue.put((shortest[v], v))
    return shortest


dijkstra_list_test = [[(1, 2), (2, 1)], [(0, 1), (3, 1)], [(0, 1), (3, 3), (4, 3), (5, 1)], [(1, 1), (2, 3), (4, 3)],
                      [(2, 3), (3, 3), (5, 2)], [(2, 1), (4, 2), (6, 2), (7, 1)], [(5, 2), (7, 3)], [(5, 1), (6, 3)]]
# correct: [0, 2, 1, 3, 4, 2, 4, 3]
print(dijkstra_list(dijkstra_list_test, 0))


def prima_list(graph):
    n = len(graph)
    shortest = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    shortest[0] = 0
    queue = PriorityQueue()
    queue.put((0, 0))
    result = []
    while not queue.empty():
        p, u = queue.get()
        if p > shortest[u]:
            continue
        if parent[u] is not None:
            result.append((u, parent[u]))
        for v, w in graph[u]:
            if shortest[v] > shortest[u] + w:
                shortest[v] = shortest[u] + w
                parent[v] = u
                queue.put((shortest[v], v))
    return result


print(prima_list(dijkstra_list_test))
# [(2, 0), (1, 0), (5, 2), (3, 1), (7, 5), (4, 2), (6, 5)]


# Zad 1. Ścieżka przechodząca przez wszystkie wierzchołki DAGu.
# Sortujemy topologicznie i sprawdzamy, czy daje to odp. ścieżkę.
def DAG_path(G):
    n = len(G)
    visited = [False for _ in range(n)]
    result = []

    def DFSVisit(v):
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                DFSVisit(u)
        result.append(v)
    for i in range(n):
        if not visited[i]:
            DFSVisit(i)

    if len(result) != n:
        return None
    # check if path is correct
    for i in range(n - 1, 0, -1):
        u = result[i]
        v = result[i - 1]
        found = False
        for j in G[u]:
            if j == v:
                found = True
                break
        if not found:
            return None
    return result[::-1]


# Zad 4. Mamy dany graf G=(V, E), w: E->R >= 1. Wartość ścieżki to iloczyn jej wag. Proszę wskazać algorytm znajdujący
# ścieżkę o najmniejszej wartości z s do t.
# Korzystamy z tego, że ln(x*y) = ln(x)+ln(y) i dla x >= 1 ln jest funkcją rosnącą. Przekształcamy tak wagi krawędzi
# i dalej algorytm Dijsktry.
def shortest_path_product(G, s, t):
    n = len(G)
    for i in range(n):
        for j in range(len(G[i])):
            G[i][j][1] = log2(G[i][j][1])

    shortest = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    shortest[s] = 0
    queue = PriorityQueue()
    queue.put((0, s))
    while not queue.empty():
        p, u = queue.get()
        if p > shortest[u]:
            continue
        for v, w in G[u]:
            if shortest[v] > shortest[u] + w:
                parent[v] = u
                shortest[v] = shortest[u] + w
                queue.put((shortest[v], v))
    result = [t]
    r = t
    while parent[r] is not None:
        result.append(parent[r])
        r = parent[r]
    return result[r::-1]
