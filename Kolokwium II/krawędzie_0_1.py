"""
Dana jest mapa kraju w postaci grafu G=(V, E). Kierowca chce przejechać z miasta (wierzchołka) s do miasta t. Niestety
niektóre drogi (krawędzie) są płatne. Każda droga ma taką samą jednostkową opłatę. Proszę podać algorytm, który znajduje
trasę wymagającą jak najmniejszej liczby opłat. W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm
dla grafu nieskierowanego.
BFS, ale jeśli znajdziem wierczhołek już odwiedzony i jak możemy zmniejszyc koszt to z powrote mgo wrzucamt do kolejki.
"""


from queue import Queue


def cheapest(graph, s, t, toll):
    n = len(graph)
    queue = Queue()
    cheap = [float('inf') for _ in range(n)]
    cheap[s] = 0
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if cheap[u] + toll[u][v] < cheap[v]:
                cheap[v] = cheap[u] + toll[u][v]
                queue.put(v)
    return cheap[t]
