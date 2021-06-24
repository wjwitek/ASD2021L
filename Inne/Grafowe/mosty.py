def dfs_matrix(matrix):
    n = len(matrix)
    visited = [False for _ in range(n)]
    time = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    timer = 1

    def visit(vertex):
        nonlocal timer
        visited[vertex] = True
        time[vertex] = timer
        timer += 1
        for i in range(n):
            if matrix[vertex][i] != 0 and not visited[i]:
                parent[i] = vertex
                visit(i)

    for j in range(n):
        if not visited[j]:
            visit(j)

    return time, parent


def low_calc(vertex, parents, times, graph, low):
    if low[vertex] is not None:
        return low[vertex]
    low[vertex] = times[vertex]
    n = len(graph)
    for i in range(n):
        if graph[vertex][i] != 0 and parents[i] != vertex and parents[vertex] != i and low[vertex] > times[i]:
            low[vertex] = times[i]
    for i in range(n):
        if parents[i] == vertex and low[vertex] > low_calc(i, parents, times, graph, low):
            low[vertex] = low_calc(i, parents, times, graph, low)
    return low[vertex]


# mosty w grafie dla reprezentacji macierzowej
def bridge(graph):
    times, parent = dfs_matrix(graph)
    n = len(graph)
    low = [None for _ in range(n)]
    for i in range(n):
        low_calc(i, parent, times, graph, low)
    result = []
    for i in range(n):
        if low[i] == times[i] and parent[i] is not None:
            result.append([i, parent[i]])
    return result


test = [
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    ]


print(bridge(test))
