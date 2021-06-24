from union import Node


# for adjacency matrix
def kruskal(graph):
    n = len(graph)
    # create list of edges
    edges = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                edges.append([i, j, graph[i]][j])
    edges.sort(key=lambda x: x[2])
    vertices = [Node(i) for i in range(n)]
    result = []
    for u, v, w in edges:
        if vertices[u].find() != vertices[v].find():
            result.append((u, v))
            vertices[u].union(vertices[v])
    return result