"""
Weronika Witek
założenie: każdy wierzchołek jest albo zielony, albo niebieski
Za pomocą algorytmu Floyda-Warshalla obliczam odległości między każdymi dwoma wierzchołkami, a następnie tworzę nowy
graf, w którym każdy węzeł zielony łącze z każdym węzłem niebieskimm który jest odległy o co najmniej d krawędzią
skierowaną o pojemności 1. Na koniec źrodło łącze z wszystkimi węzłami o kolorze zielonym krawędziami o pojemności 1 i
podobnie wszystkie węzły niebieskie z ujściem. Maksymalny przepływ między źródłem a ujściem jest równy liczbie par. (bo
przepływ przez wierzchołki niebieskie i zielone równy max 1 oznacza, że mogą być w najwyzej jednej parze)
Złoźoność czasowa: O(VE^2) - złożoność algorytmu Edmondsa-Karpa
"""
from zad3testy import runtests
from zad3EK import edmonds_karp


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


def BlueAndGreen(T, K, D):
    n = len(T)
    # konstrukcja nowego grafu (źródłu przypisuje indeks n, a ujściu n + 1)
    graph = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    shortest = floyd_warshall(T)
    for i in range(n):
        if K[i] == 'G':
            graph[n][i] = 1
            for j in range(n):
                if K[j] == 'B' and shortest[i][j] >= D:
                    graph[i][j] = 1
        else:
            graph[i][n + 1] = 1
    return edmonds_karp(graph, n, n + 1)


runtests(BlueAndGreen)
