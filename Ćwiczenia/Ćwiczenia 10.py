from queue import PriorityQueue


"""
Zad obowiązkowe 1: Dany jest graf nieskierowany G = (V,E) z ważonymi krawędziami (w: E -> N). Proszę zaproponować
jak najszybszy algorytm, który znajduje ścieżkę z danego wierzchołka s do danego wierzchołka t taką, że:
- Każda kolejne krawędź ma mniejszą wagę niż poprzednia
- Spośród ścieżek spełniających powyższy warunek, znaleziona ma najmniejszą sumę wag
Pomysł: Algorytm Dijsktry, ale do kolejki wrzucamy trójki (długość ścieżki, wierzchołek, krawędź pochodzenia).
Złożoność czasowa: O(ElogE) ~ O(ElogV)
"""


# for adjacency list
def decreasing_path(graph, s, t):
    n = len(graph)
    queue = PriorityQueue()
    parent = [[None for _ in range(n)] for _ in range(n)]
    shortest = [[float('inf') for _ in range(n)] for _ in range(n)]
    for u, w in graph[s]:
        queue.put((w, u, w, u))
        shortest[s][u] = 0
    while not queue.empty():
        path_length, v, edge_before, v_before = queue.get()
        for u, w in graph[v]:
            if shortest[v][u] > path_length and edge_before > w:
                shortest[v][u] = path_length
                parent[v][u] = v_before
                queue.put((path_length + w, u, w, v))
    # find best path and recreate it
    smallest = 0
    for i in range(1, n):
        if shortest[i][t] < shortest[smallest][t]:
            smallest = i
    if shortest[smallest][t] == float('inf'):
        return None
    result = [t]
    v = t
    while parent[smallest][v] is not None:
        result.append(smallest)
        v, smallest = smallest, parent[smallest][v]
    result.append(s)
    return result[::-1]


# # [0, 2, 4, 3]
# G1 = [
#     [[2, 100], [1, 4]],  # 0
#     [[0, 4], [4, 3]],   # 1
#     [[3, 200], [0, 100], [4, 4]],   # 2
#     [[2, 200], [4, 3]],  # 3
#     [[2, 4], [1, 3], [3, 3]]  # 4
# ]
# print(decreasing_path(G1, 0, 3))
#
# # [0, 3, 2]
# G2 = [[(1, 10), (3, 4)],  # 0
#       [(0, 10), (2, 10)],  # 1
#       [(1, 10), (3, 3)],  # 2
#       [(0, 4), (2, 3)]]  # 3
#
# print(decreasing_path(G2, 0, 2))



"""
Zad obowiązkowe 2: Dany jest graf skierowany G = (V,E) w reprezentacji macierzowej (bez wag). Proszę zaimplementować 
algorytm, który oblicza domknięcie przechodnie grafu G (domknięcie przechodnie grafu G to takie graf H, że w H mamy 
krawędź z u do v wtedy i tylko wtedy gdy w G jest ścieżka skierowana z u do v).
Pomysł:
- obliczamy odległosći między każdą parą wierzchołków
- jeśli jest rózna od -1 to w domknięciu przechodnim ma być krawędź
Złożoność obliczeniowa: O(V^3)
"""


# for adjacency matrix
def transitive_closure(G):
    n = len(G)
    # distance between each two vertices
    shortest = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                shortest[i][j] = 1
    for i in range(n):
        for j in range(n):
            for k in range(n):
                shortest[j][k] = min(shortest[j][k], shortest[j][i] + shortest[i][k])
    for i in range(n):
        for j in range(n):
            if shortest[i][j] == float('inf'):
                shortest[i][j] = 0
            else:
                shortest[i][j] = 1
    return shortest


# G3 = [[0, 1, 0, 0, 0], [0, 0, 1, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
# for row in transitive_closure(G3):
#     print(row)
#
# G4 = [[0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# for row in transitive_closure(G4):
#     print(row)


# for list of edges
def decreasing_path_v2(graph, start, t):
    # find number of nodes
    m = len(graph)
    n = 0
    for i in range(m):
        n = max(n, graph[i][0], graph[i][1])
    n += 1

    # sort edges by weight (decreasing order)
    graph.sort(key=lambda x: x[2], reverse=True)

    # go through edges
    shortest = [float('inf') for _ in range(n)]
    parent = [[] for _ in range(n)]
    shortest[start] = 0
    for i in range(m):
        u, v, w = graph[i]
        if shortest[u] + w < shortest[v]:
            shortest[v] = shortest[u] + w
            parent[v].append([u, w, shortest[v]])
        elif shortest[v] + w < shortest[u]:
            shortest[u] = shortest[v] + w
            parent[u].append([v, w, shortest[u]])

    # recreate result based on parents
    if not parent[t]:
        return []
    result = [t]
    prev_val = shortest[t]
    prev_edge = parent[t][len(parent[t]) - 1][1]
    t = parent[t][len(parent[t]) - 1][0]
    while parent[t]:
        result.append(t)
        i = len(parent[t]) - 1
        u, w, s = parent[t][i]
        while prev_val - prev_edge != s:
            i -= 1
            u, w, s = parent[t][i]
        prev_val = s
        prev_edge = w
        t = u
    result.append(start)
    return result[::-1]


# G = [(0, 1, 4), (1, 2, 10), (0, 4, 8), (1, 4, 11), (4, 5, 7), (4, 6, 4), (5, 6, 6), (2, 3, 2), (2, 5, 9), (3, 6, 3),
#      (6, 7, 5), (3, 7, 15), (3, 8, 8), (7, 8, 1)]
# print(decreasing_path_v2(G, 0, 8))


"""
Zadanie 1. (SAT-2CNF) Dana jest formuła logiczna w postaci 2CNF. To znaczy, ze formuła jest
koniunkcja klauzuli, gdzie kazda klauzula to alternatywa dwóch literałów, a kazdy literał to zmienna lub jej
negacja. Przykładem formuły w postaci 2CNF nad zmiennymi x,y,z jest:
(x v y) , (not x v z) , (not z v not y).
Prosze podac algorytm, który w czasie wielomianowym stwierdza, czy istnieje wartosciowanie spełniajace
formułe.
Pomysł:
- każdą klauzulę przekształcamy do postaci implikacji
- tworzymy graf skierowany gdzie x -> y oznacza, że z x wynika y
- dzielimy graf na spójne składowe
- jeśli w ramach jednej składowej istnieje x oraz not x, to formuła nie jest spełnialna, w przeciwnym wypadku jest
spełnialna
"""


# tab is 2d array of clauses x v y = ['x', 'y']
def SAT_2CNF(tab):
    # find all unique variables (x and not x are counted as the same) and sort them alphabetically
    variables = []
    for x, y in tab:
        if 'not' in x:
            x = x.split()[1]
        if 'not' in y:
            y = y.split()[1]
        if x not in variables:
            variables.append(x)
        if y not in variables:
            variables.append(y)
    variables.sort()
    n = len(variables)
    # create graph (adjacency matrix), if x is on index t, tha not x is on index n + t
    graph = [[0 for _ in range(2 * n)] for _ in range(2 * n)]
    for x, y in tab:
        if 'not' in x:
            x = x.split()[1]
            t = variables.index(x)
            if 'not' in y:
                y = y.split()[1]
                p = variables.index(y)
                graph[t][p + n] = 1
            else:
                p = variables.index(y)
                graph[t][p] = 1
        else:
            t = variables.index(x)
            if 'not' in y:
                y = y.split()[1]
                p = variables.index(y)
                graph[t + n][p + n] = 1
            else:
                p = variables.index(y)
                graph[t + n][p] = 1
