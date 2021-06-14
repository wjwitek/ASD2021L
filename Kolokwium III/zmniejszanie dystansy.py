"""
Dany jest graf ważony z dodatnimi wagami G. Dana jest też lista E’ krawędzi, które nie należą do grafu, ale są
krawędziami między wierzchołkami z G. Dane są również dwa wierzchołki s i t. Podaj algorytm, który stwierdzi, którą
jedną krawędź z E’ należy wszczepić do G, aby jak najbardziej zmniejszyć dystans między s i t. Jeżeli żadna krawędź nie
poprawi dystansu między s i t, to algorytm powinien to stwierdzić.
Pomysł:
Za pomocą algorytmu Floyda-Warshalla obliczamy najkrótsze ścieżki między każdymi dwoma wierchołkami, a następnie dla
każdej krawędzi ze zbioru E' sprawdzamy, czy dodanie tej krawędzi zmniejszy dystans.
Założenie: krawędzi w zbiorze E' są nieskierowane.
Złożoność czasowa: O(V^3)
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


def improve_path(graph, edges, s, t):
    shortest = floyd_warshall(graph)
    minimum = shortest[s][t]
    best_u, best_v = -1, -1
    for u, v, value in edges:
        if minimum > shortest[s][u] + shortest[v][t] + value:
            minimum = shortest[s][u] + shortest[v][t] + value
            best_u, best_v = u, v
        if minimum > shortest[s][v] + shortest[u][t] + value:
            minimum = shortest[s][v] + shortest[u][t] + value
            best_u, best_v = v, u
    return best_u, best_v
