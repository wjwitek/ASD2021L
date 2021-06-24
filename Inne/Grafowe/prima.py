def get_index(weight, visited):
    n = len(weight)
    minimum = float('inf')
    index = None
    for i in range(n):
        if weight[i] < minimum and not visited[i]:
            minimum = weight[i]
            index = i
    return index


# for adjacency matrix
def prima(graph):
    n = len(graph)
    weight = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    index = get_index(weight, visited)
    while index is not None:
        visited[index] = True
        for i in range(n):
            if not visited[i] and graph[index][i] != 0 and graph[index][i] < weight[i]:
                weight[i] = graph[index][i]
                parent[i] = index
        index = get_index(weight, visited)
    return parent
