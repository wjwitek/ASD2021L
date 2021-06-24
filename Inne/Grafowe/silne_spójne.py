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


# find strongly connected components for graph represented as adjacency matrix
def sss(graph):
    times = dfs_matrix(graph)
    n = len(graph)
    # reverse graph
    reversed_graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                reversed_graph[j][i] = graph[i][j]

    result = []
    visited = [False for _ in range(n)]
    times = [[times[x], x] for x in range(n)]
    times.sort(reverse=True)

    def visit(vertex, sign):
        visited[vertex] = True
        result[sign].append(vertex)
        for i in range(n):
            if reversed_graph[vertex][i] != 0 and not visited[i]:
                visit(i, sign)

    sign = 0
    for _, i in times:
        if not visited[i]:
            result.append([])
            visit(i, sign)
            sign += 1
    return result


test = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]

temp = sss(test)
for row in temp:
    print(row)
