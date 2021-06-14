# for adjacency list
def dfs_adjacency(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    time = [-1 for _ in range(n)]
    timer = 0

    def visit(v):
        nonlocal timer
        visited[v] = True
        time[v] = timer
        timer += 1
        for u in graph[v]:
            if not visited[u]:
                visit(u)

    for i in range(n):
        if not visited[i]:
            visit(i)

    return time


# for adjacency matrix
def dfs_matrix(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    time = [-1 for _ in range(n)]
    timer = 0

    def visit(v):
        nonlocal timer, n
        visited[v] = True
        time[v] = timer
        timer += 1
        for j in range(n):
            if not visited[j] and graph[v][j]:
                visit(j)

    for i in range(n):
        if not visited[i]:
            visit(i)

    return time
