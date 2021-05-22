from queue import PriorityQueue


# implementation of family of disjoint sets
class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


# implementation of Kruskal algorithm for list of edges
def Kruskal_edges(edges, n):
    # edges is a list ot tuples: (u, v, w({u, v}))
    # n - number of vertices in graph
    edges.sort(key=lambda x: x[2])
    vertices = [Node(i) for i in range(n)]
    result = []
    for u, v, w in edges:
        if find(u) != find(v):
            result.append((u, v))
            union(Node(u), Node(v))
    return result


# implementation of Dijkstra algorithm for adjacency matrix
def Dijkstra_matrix(graph, source):
    n = len(graph)
    shortest = [float('inf') for _ in range(n)]
    shortest[source] = 0
    queue = PriorityQueue()
    queue.put((0, source))
    while not queue.empty():
        p, u = queue.get()
        if p > shortest[u]:
            continue
        for i in range(n):
            if i == u:
                continue
            if graph[u][i] != 0 and shortest[i] > shortest[u] + graph[u][i]:
                shortest[i] = shortest[u] + graph[u][i]
                queue.put((shortest[i], i))
    return shortest


matrix = [[0, 2, 1, 0, 0, 0, 0, 0], [2, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 3, 3, 1, 0, 0], [0, 1, 3, 0, 3, 0, 0, 0],
          [0, 0, 3, 4, 0, 2, 0, 3], [0, 0, 1, 0, 2, 0, 2, 1], [0, 0, 0, 0, 0, 2, 0, 3], [0, 0, 0, 0, 3, 1, 3, 0]]
# correct: [0, 2, 1, 3, 4, 2, 4, 3]
print(Dijkstra_matrix(matrix, 0))