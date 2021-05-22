"""
Dany jest graf G=(V, E), gdzie każda krawędź ma wagę ze zbioru {1, . . . ,E} (wagi krawędzi są parami różne). Proszę
zaproponować algorytm, który dla danych wierzchołków x i y sprawdza, czy istnieje ścieżka z x do y, w której
przechodzimy po krawędziach o coraz mniejszych wagach.
BFS, jeśli wierzchołek do którego dochodzimy może mieć rodzica o większej wadze to podmieniamy i wsadzamy wierczhołek
z powrotem do kolejki.
"""


from queue import Queue


# zakładam, że graf skierowany i w formie list sąsiedztwa
def decreasing_path(graph, x, y, values):
    n = len(graph)
    queue = Queue()
    highest = [-1 for _ in range(n)]
    highest[x] = values[x]
    queue.put(x)
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if values[v] < values[u] and values[u] > highest[v]:
                highest[v] = values[u]
                queue.put(v)
                if v == y:
                    return True
    return False
