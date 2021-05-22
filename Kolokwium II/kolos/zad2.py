from zad2testy import runtests
from queue import PriorityQueue


def enlarge(G, s, t):
    n = len(G)
    # znajdź długość nakrótszej ścieżki
    queue = PriorityQueue()
    priority = 0
    visited = [-1 for _ in range(n)]
    prev = [[] for _ in range(n)]
    parent = [None for _ in range(n)]
    queue.put((priority, s))
    priority += 1
    visited[s] = 0
    stop = False
    while not queue.empty():
        _, u = queue.get()
        for v in G[u]:
            if visited[v] == -1:
                visited[v] = visited[u] + 1
                parent[v] = u
                queue.put((priority, v))
                priority += 1
    for row in prev:
        print(row)
    print(visited)
    print(parent)
    shortest = visited[t]
    if shortest == -1:
        return None
    # policz ile jest najkrótszych ścieżek
    counter = 1
    flag = False
    check = [False for _ in range(n)]
    queue_prim = PriorityQueue()
    priority_prim = 0
    step = visited[t] - 1
    queue.put((priority, t))
    switch = True
    while True:
        while not queue.empty():
            v = queue.get()
            for u in G[v]:
                if visited[u] == step:
                    queue_prim.put((priority_prim, u))
                    priority_prim += 1
                    visited[u] = -2


runtests( enlarge )
