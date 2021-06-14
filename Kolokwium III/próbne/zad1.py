"""
Biorę maksimum z macierzy odległości z algorytmu Floyda-Warshalla.  O(V^3)
(Pomijając inf oczywiście.)
"""
from zad1testy import runtests


def floyd_warshall(graph):
    n = len(graph)
    shortest = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                shortest[i][j] = float('inf')
            else:
                shortest[i][j] = graph[i][j]
    for t in range(n):
        for u in range(n):
            for v in range(n):
                if shortest[u][t] + shortest[t][v] < shortest[u][v]:
                    shortest[u][v] = shortest[u][t] + shortest[t][v]
    return shortest


def przekatna_w_grafie(G) -> int:
    n = len(G)
    if n == 0:
        return None
    tab = floyd_warshall(G)
    maximum = -1
    for i in range(n):
        for j in range(n):
            if tab[i][j] != float('inf') and tab[i][j] > maximum:
                maximum = tab[i][j]
    if maximum == -1:
        return None
    return maximum


runtests(przekatna_w_grafie)
