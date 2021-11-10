"""
Jeśli dobrze rozumiem, to zadanie sprowadza się do znalezienie najkrótszego cyklu w grafie skierowanym.
Dla każdej krawędzi (i, j) szukam najkrótsej ściezki z i do j za pomocą algorytmu Dijkstry.
Złożoność czasowa: O(V^4)
"""

from zad3_testy import run_tests


def get_index(shortest, visited):
    n = len(shortest)
    index = None
    minimum = float('inf')
    for i in range(n):
        if not visited[i] and shortest[i] < minimum:
            minimum = shortest[i]
            index = i
    return index


def dijkstra_matrix(graph, source):
    n = len(graph)
    shortest = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    shortest[source] = 0
    index = get_index(shortest, visited)
    while index is not None:
        for i in range(n):
            if i == index:
                continue
            if not visited[i] and graph[index][i] != 0 and shortest[i] > shortest[index] + graph[index][i]:
                shortest[i] = shortest[index] + graph[index][i]
                parent[i] = index
        visited[index] = True
        index = get_index(shortest, visited)
    return shortest, parent


def get_path(parent, i):
    result = []
    while i is not None:
        result.append(i)
        i = parent[i]
    return result[::-1]


def gorszy_mag(G) -> list:
    n = len(G)
    minimum = float('inf')
    result = None
    temp = None
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if G[i][j] != 0:
                value = G[i][j]
                G[i][j] = 0
                value_2 = G[j][i]
                G[j][i] = 0
                shortest, parent = dijkstra_matrix(G, j)
                temp = get_path(parent, i)
                if value + shortest[i] < minimum and len(temp) > 2:
                    minimum = value + shortest[i]
                    result = get_path(parent, i)
                G[i][j] = value
                G[j][i] = value_2
    if minimum == float('inf'):
        minimum = None
    return [minimum, result]



run_tests(gorszy_mag)
