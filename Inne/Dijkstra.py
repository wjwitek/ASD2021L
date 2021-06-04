from queue import PriorityQueue


# Dijkstra algorithm for adjacency list
def dijkstra_list(graph, source):
    n = len(graph)
    shortest = [float('inf') for _ in range(n)]
    shortest[source] = 0
    queue = PriorityQueue()
    queue.put((0, source))
    while not queue.empty():
        p, u = queue.get()
        if p > shortest[u]:
            continue
        for v, w in graph[u]:
            if shortest[v] > shortest[u] + w:
                shortest[v] = shortest[u] + w
                queue.put((shortest[v], v))
    return shortest


# Dijkstra algorithm for adjacency matrix
def dijkstra_matrix(graph, source):
    n = len(graph)
    shortest = [float('inf') for _ in range(n)]
    shortest[source] = 0
    queue = PriorityQueue()
    queue.put((0, source))
    while not queue.empty():
        p, u = queue.get()
        if p > shortest[u]:
            continue
        for i in range(n):
            if graph[u][i] != 0 and shortest[i] > shortest[u] + graph[u][i]:
                shortest[i] = shortest[u] + graph[u][i]
                queue.put((shortest[i], i))
    return shortest
