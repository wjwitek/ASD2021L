# Weronika Witek
# złożoność czasowa: O(n^2), gdzie n to liczba wierzchołków, bo: n^2 - dodanie wierzchołków do kolejki plus e - czyli
# liczba krawędzi i złożoność czasowa utworzenia cyklu (liczba razy kiedy trafimy na przetworozny wierzchołek),
# ale e < n^2
# złożoność pamięciowa: O(e), gdzie e to liczba krawędzi
from copy import deepcopy
from collections import deque
from queue import PriorityQueue


def is_euler(edges):
    # if all nodes have even degree return True, else return False
    n = len(edges)
    for i in range(n):
        degree = 0
        for j in range(n):
            if edges[i][j]:
                degree += 1
        if degree % 2:
            return False
    return True


def euler(matrix):
    # check if graph has euler cycle
    if not is_euler(matrix):
        return None
    n = len(matrix)
    # using array of indexes to not start from index 0 each time I'm looking for not used edge (lines 39-40)
    index = [0 for _ in range(n)]
    # priority queue, but used as FIFO queue (by decreasing priority each time new element is added)
    queue = PriorityQueue()
    p = 0
    queue.put((p, 0))
    p -= 1
    result = deque()
    while not queue.empty():
        current = queue.get()[1]
        # look for not used edge
        while index[current] < n and matrix[current][index[current]] != 1:
            index[current] += 1
        # if node was processed (all its edges are marked as used) add it to result
        if not index[current] < n:
            result.appendleft(current)
        # if not go to next possible node (first add current node back to queue)
        else:
            queue.put((p, current))
            p -= 1
            queue.put((p, index[current]))
            p -= 1
            # mark edge between current and index[current] as already used
            matrix[current][index[current]] = 2
            matrix[index[current]][current] = 2
        index[current] += 1
    # repair matrix
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 2:
                matrix[i][j] = 1
    return list(result)


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

GG = deepcopy(G)
cycle = euler(G)

if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")

