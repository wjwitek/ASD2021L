from copy import deepcopy


# with parent field
def floyd_warshall(graph):
    n = len(graph)
    shortest = [[-1 for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]
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
                    parent[u][v] = parent[t][v]
    return shortest, parent
