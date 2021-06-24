# top sort for adjacency matrix
def dfs_matrix(matrix):
    n = len(matrix)
    visited = [False for _ in range(n)]
    time = [-1 for _ in range(n)]
    timer = 0

    def visit(vertex):
        nonlocal timer
        visited[vertex] = True
        for i in range(n):
            if matrix[vertex][i] != 0 and not visited[i]:
                visit(i)
        time[vertex] = timer
        timer += 1

    for j in range(n):
        if not visited[j]:
            visit(j)

    return time


# top sort for adjacency list
def dfs_list(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    time = [-1 for _ in range(n)]
    timer = 0

    def visit(vertex):
        nonlocal timer
        visited[vertex] = True
        for i in graph[vertex]:
            if not visited[i]:
                visit(i)
        time[vertex] = timer
        timer += 1

    for j in range(n):
        if not visited[j]:
            visit(j)

    return time
