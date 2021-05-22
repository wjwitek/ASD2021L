from queue import Queue


# BFS implementation for adjacency matrix, start is a node algorithm starts from
def BFS_matrix(matrix, start):
    n = len(matrix)
    nodes_queue = Queue(n)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited[start] = True
    distance[start] = 0
    nodes_queue.put(start)
    while not nodes_queue.empty():
        current = nodes_queue.get()
        for i in range(n):
            if matrix[current][i] and not visited[i]:
                visited[i] = True
                distance[i] = distance[current] + 1
                parent[i] = current
                nodes_queue.put(i)
    print(visited)
    print(distance)
    print(parent)


# BFS implementation for adjacency list, start is a node algorithm starts from
def BFS_list(graph, start):
    n = len(graph)
    queue = Queue()
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited[start] = True
    distance[start] = 0
    queue.put(start)
    while not queue.empty():
        current = queue.get()
        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[current] + 1
                parent[i] = current
                queue.put(i)
    print(visited)
    print(distance)
    print(parent)
