"""
Weronika Witek
Obliczam odległości pomiędzy każdymi dwom wierzchołkami (Floyd-Warshall). Następnie tworzę nowy graf w którym
wierzchołkami są pary wierzchołków - pary w których aktualnie znajduja się odpowiednio Carol i Max. Krawędź z
wierzchołka (a, b) do wierzchołka (c, d) istnieje (i ma wagę 1) wtedy i tylko wtedy, gdy spełnione są
następujące warunki:
(D ozancza minimalną odległość)
- a != b i c != d i ~(a == d i b == c)
- distance[a][b] >= D i distance[c][d] >= D
- (a == c i {b, d} ∈ E) lub (b == d i {a, c} ∈ E) lub ({b, d} ∈ E i {a, c} ∈ E)
A więc jeśli ciężarówki mogą bezpiecznie przebywac w wierzchołku i istniej przejazd do koljnego wierzchołka.
Następnie w nowym grafie szukam ścieżki z (x, y) do (y, x) za pomocą DFS wypełniając pola parent.
Złożoność czasowa: O(V^4)
(O(V^3) - Floyd-Warshall, O(V^4) - utworzenie nowego grafu, O(V^2+V^4) - DFS na nowym grafie)
"""
from zad1testy import runtests


def DFS(matrix, xy):
    n = len(matrix)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    def visit(v):
        visited[v] = True
        for i in range(n):
            if matrix[v][i] != 0 and not visited[i]:
                parent[i] = v
                visit(i)

    visit(xy)
    return parent


def floyd_warshall(graph):
    n = len(graph)
    shortest = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                shortest[i][j] = 0
            elif graph[i][j] == 0:
                shortest[i][j] = float('inf')
            else:
                shortest[i][j] = graph[i][j]
    for t in range(n):
        for u in range(n):
            for v in range(n):
                if shortest[u][t] + shortest[t][v] < shortest[u][v]:
                    shortest[u][v] = shortest[u][t] + shortest[t][v]
    return shortest


def keep_distance(M, x, y, d):
    D = d
    distance = floyd_warshall(M)
    n = len(M)
    # create new graph, parę wierzchołków (i, j) oznacza indeks i * n + j (jak w linearyzacji tablicy 2D)
    graph = [[0 for _ in range(n * n)] for _ in range(n * n)]
    for a in range(n):
        for b in range(n):
            if distance[a][b] >= D:
                for c in range(n):
                    for d in range(n):
                        if distance[c][d] >= D and not (a == c and b == d) and not (a == d and b == c):
                            if a == c and M[b][d] != 0:
                                graph[a * n + b][c * n + d] = 1
                            elif b == d and M[a][c] != 0:
                                graph[a * n + b][c * n + d] = 1
                            elif M[b][d] != 0 and M[a][c] != 0:
                                graph[a * n + b][c * n + d] = 1
    parent = DFS(graph, x * n + y)
    result = []
    current = y * n + x
    while current is not None:
        temp = (current // n, current % n)
        result.append(temp)
        current = parent[current]
    return result[::-1]


runtests(keep_distance)