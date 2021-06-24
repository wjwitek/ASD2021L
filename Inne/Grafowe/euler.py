from copy import deepcopy


# find euler cycle in undirected graph represented as matrix
def euler_cycle_undirected(graph):
    n = len(graph)
    # check if euler cycle is possible
    for i in range(n):
        counter = 0
        for j in range(n):
            if graph[i][i] != 0:
                counter += 1
        if counter % 2 == 1:
            return None
    # find the cycle
    graph_copy = deepcopy(graph)
    result = []

    def visit(vertex):
        for k in range(n):
            if graph_copy[vertex][k]:
                graph_copy[vertex][k] = 0
                graph_copy[k][vertex] = 0
                visit(k)
        result.append(vertex)

    visit(0)
    return result[::-1]
