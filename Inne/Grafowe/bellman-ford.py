# for adjacency matrix - assumption: float('inf) means no edge
def bellman_ford_matrix(graph, source):
    n = len(graph)
    distance = [float('inf') for _ in range(n)]
    distance[source] = 0
    # calculate distances
    for k in range(n - 1):
        for i in range(n):
            for j in range(n):
                if graph[i][j] != float('inf') and distance[j] > distance[i] + graph[i][j]:
                    distance[j] = distance[i] + graph[i][j]
    # verify if there are no negative cycles
    for i in range(n):
        for j in range(n):
            if graph[i][j] != float('inf') and distance[j] > distance[i] + graph[i][j]:
                return None  # means negative cycle was found
    return distance


"""
test_matrix = [[float('inf'), 2, -1, 1, float('inf'), float('inf')],
               [float('inf'), float('inf'), float('inf'), float('inf'), -2, float('inf')],
               [float('inf'), 3, float('inf'), float('inf'), -1, float('inf')],
               [float('inf'), float('inf'), -3, float('inf'), float('inf'), float('inf')],
               [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2],
               [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]]
print(bellman_ford_matrix(test_matrix, 0))
"""


# bellman-ford algorithm for adjacency list
def bellman_ford_list(graph, source):
    n = len(graph)
    distance = [float('inf') for _ in range(n)]
    distance[source] = 0
    # calculate distances
    for k in range(n - 1):
        for i in range(n):
            for j, w in graph[i]:
                if distance[j] > distance[i] + w:
                    distance[j] = distance[i] + w
    # verify if there are no negative cycles
    for i in range(n):
        for j, w in graph[i]:
            if distance[j] > distance[i] + w:
                return None  # means negative cycle was found
    return distance
