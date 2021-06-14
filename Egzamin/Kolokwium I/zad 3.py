"""
Problem can be rephrased as finding euler path that starts in X and ends in Y, in directed graph. This is possible
if and only if following conditions are met:
- X out degree is exactly one more than X in degree
- Y in degree is exactly one more than Y out degree
- for every other node: in degree is equal to out degree
To create euler path from X to Y:
- find shortest path from X to Y using BFS and represent it as linked list
- find cycles and add them to path until all edges are visited (loop going through nodes of path made so far until all
edges are used)
Time complexity: ? nie wiem, nie umiem ocenić złożoności tego czegoś co dodaje pętle do ścięzki xD
"""
from collections import deque


class Path:
    def __init__(self, node):
        self.node = node
        self.next = None


def not_all_used(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                return True
    return False


def all_visited(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i] == 1:
                return False
    return True


def darmowe_przejazdy_XD(T, X, Y):
    # find number of nodes
    m = len(T)
    n = 0
    for i in range(m):
        n = max(n, T[i][0], T[i][1])
    n += 1
    # check if it is possible to find path
    degree = [0 for _ in range(n)]
    for u, v in T:
        degree[u] -= 1
        degree[v] += 1
    for i in range(n):
        if i == X:
            if degree[i] != -1:
                return False
        elif i == Y:
            if degree[i] != 1:
                return False
        else:
            if degree[i] != 0:
                return False
    # create adjacency matrix
    graph = [[0 for _ in range(n)] for _ in range(n)]
    parent = [None for _ in range(n)]
    for u, v in T:
        graph[u][v] = 1
    # find direct path to Y from X using BFS
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[X] = True
    queue = deque()
    queue.append(X)
    counter = 1
    while counter > 0:
        node = queue.popleft()
        counter -= 1
        for i in range(n):
            if not visited[i] and graph[node][i] == 1:
                queue.append(i)
                parent[i] = node
                visited[i] = True
                counter += 1
    # create path using linked list and mark its edges as visited
    first = None
    temp = Y
    while parent[temp] is not None:
        new_node = Path(temp)
        new_node.next = first
        first = new_node
        graph[parent[temp]][temp] = -1
        temp = parent[temp]
    new_node = Path(X)
    new_node.next = first
    first = new_node
    # add cycles to graph
    while not_all_used(graph):
        r = first
        while r is not None:
            for i in range(n):
                if graph[r.node][i] == 1:
                    # find cycle
                    cycle_first = Path(i)
                    graph[r.node][i] = -1
                    temp = cycle_first
                    while temp.node != r.node:
                        for j in range(n):
                            if graph[temp.node][j] == 1:
                                graph[temp.node][j] = -1
                                new_node = Path(j)
                                temp.next = new_node
                                temp = new_node
                    # add cycle to path
                    temp.next = r.next
                    r.next = cycle_first
            r = r.next
    # turn linked list into array
    path = []
    while first is not None:
        path.append(first.node)
        first = first.next
    return path


if __name__ == "__main__":
    from zad3testy import runtests
    runtests(darmowe_przejazdy_XD)

G6 = [(1, 2), (1, 0), (2, 5), (2, 3), (3, 7), (3, 4), (0, 2), (0, 5), (0, 6), (5, 8), (5, 3), (5, 7), (6, 5),
      (7, 0), (7, 1), (8, 0)]
a6, b6 = 1, 4
odp6 = [1, 0, 2, 5, 7, 0, 5, 0, 6, 5, 3, 7, 1, 2, 3, 4]  # przy czym jest to odp przykładowa, jest kilka możliwości

G7 = [(0, 1), (0, 3), (1, 2), (1, 5), (5, 6), (6, 3), (3, 1), (3, 4), (4, 0)]
a7, b7 = 0, 2
odp7 = [0, 3, 4, 0, 5, 6, 0, 1, 2]

G8 = [(0, 1), (1, 2), (2, 3), (3, 2), (3, 4), (2, 5), (5, 3)]
a8, b8 = 0, 4
odp8 = [0, 1, 2, 3, 2, 5, 3, 4]

print(darmowe_przejazdy_XD(G6, 1, 4))
print(darmowe_przejazdy_XD(G7, a7, b7))
print(darmowe_przejazdy_XD(G8, a8, b8))
