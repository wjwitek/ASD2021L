"""
Dany jest graf ważony z dodatnimi wagami. Należy podać algorytm, który zwróci długość
najkrótszego cyklu w grafie. Należy podać rozwiązania dla grafów rzadkich i gęstych. Algorytm
powinien stwierdzić, jeśli graf nie ma cyklu.
Pomysł: Obliczam odległość między każdymi dwoma wierzchołkami w grafie za pomocą algorytmu Floyda-Warshalla. Następnie
dla każdej krawędzi, jeśli nie stanowi ona ścieżki pomiędzy tymi wierzchołkami, sprawdzamy czy tworzy ona z ścieżką
między tymi wierzchołkami szukany najmniejszy.
"""


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


def shortest_cycle(graph):
    n = len(graph)
    shortest = floyd_warshall(graph)
    minimum = float('inf')
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and graph[i][j] != shortest[j][i] and minimum > shortest[j][i] + graph[i][j]:
                minimum = shortest[j][i] + graph[i][j]
            if graph[j][i] != 0 and graph[j][i] != shortest[i][j] and minimum > shortest[i][j] + graph[j][i]:
                minimum = shortest[i][j] + graph[j][i]
    if minimum == float('inf'):
        return None
    return minimum
