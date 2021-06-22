# top sort for adjacency matrix
def topsort_matrix(matrix):
    n = len(matrix)
    visited = [False for _ in range(n)]
    result = []

    def visit(vertex):
        visited[vertex] = True
        for i in range(n):
            if matrix[vertex][i] != 0 and not visited[i]:
                visit(i)
        result.append(vertex)

    for j in range(n):
        if not visited[j]:
            visit(j)

    return result[::-1]


# top sort for adjacency list
def topsort_list(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    result = []

    def visit(vertex):
        visited[vertex] = True
        for i in graph[vertex]:
            if not visited[i]:
                visit(i)
        result.append(vertex)

    for j in range(n):
        if not visited[j]:
            visit(j)

    return result[::-1]
