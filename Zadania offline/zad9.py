"""
Weronika Witek
f(i, j) = -1 jeśli nie ma krawędzi {i, j}, a jeśli jest to jest to długość najkrótszej ścieżki pomiędzy i a j nie
zawierająca {i, j}, tej najkrótszej ścieżki szukamy używając algorytmu Dijkstry (przy czym nie przechowujemy
wszystkich wartości f(i, j), a tylko tą dla najkrótszego dotychczas znalezionego cyklu i tablicę parent dla tego cyklu)
długość szukanego cyklu: min po i,j {f(i, j) + w({i, j})}
złozoność czasowa: O[E(E+V)logV+V^2]:
- E(E+V)logV - algorytm Dijkstry dla E krawędzi przy reprezentacji macierzowej
- V^2 - przejście po macierzy w celu znelezienia wszystkich krawędzi
złożoność pamięciowa: O(V)
"""
from copy import deepcopy
from queue import PriorityQueue


def min_cycle(G):
    n = len(G)
    shortest = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    queue = PriorityQueue()
    shortest_cycle = float('inf')
    shortest_cycle_parent = [None for _ in range(n)]
    shortest_cycle_start = -1
    for i in range(n):
        for j in range(i + 1, n):  # from i + 1, because f(i, j) = f(j, i)
            if G[i][j] != -1:
                # reset arrays
                for k in range(n):
                    shortest[k] = float('inf')
                    parent[k] = None
                # temporarily delete edge from matrix
                edge_value = G[i][j]
                G[i][j] = G[j][i] = -1
                # Dijkstra algorithm starting at i
                shortest[i] = 0
                queue.put((0, i))
                while not queue.empty():
                    w, ver = queue.get()
                    if w > shortest[ver]:
                        continue
                    for k in range(n):
                        if k == ver:
                            continue
                        if G[ver][k] != -1 and shortest[k] > shortest[ver] + G[ver][k]:
                            shortest[k] = shortest[ver] + G[ver][k]
                            queue.put((shortest[k], k))
                            parent[k] = ver
                # repair matrix
                G[i][j] = G[j][i] = edge_value
                # check if cycle including {i, j} exists and is it better choice
                if shortest[j] != float('inf') and shortest[j] + G[i][j] < shortest_cycle:
                    shortest_cycle = shortest[j] + G[i][j]
                    for k in range(n):
                        shortest_cycle_parent[k] = parent[k]
                    shortest_cycle_start = j
    # recreate result
    if shortest_cycle == float('inf'):
        return []
    result = []
    i = shortest_cycle_start
    while i is not None:
        result.append(i)
        i = shortest_cycle_parent[i]
    return result


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]
LEN = 7

GG = deepcopy(G)
cycle = min_cycle(GG)

print("Cykl :", cycle)

if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:] + [u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")
