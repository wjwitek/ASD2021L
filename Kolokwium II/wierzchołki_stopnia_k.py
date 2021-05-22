"""
NiechG= (V, E) będzie pewnym grafem nieskierowanym, a U⊆V pewnym podzbiorem jego wierzchołków. Grafem indukowanym G|U
nazywamy graf powstały z G przez usunięcie wszystkich wierzchołków spoza U. Proszę podać i zaimplementować wielomianowy
algorytm, który mając na wejściu graf G= (V, E) (reprezentacja przez listy sąsiedztwa) oraz liczbę naturalną k, znajduje
maksymalny co do rozmiaru zbiór U⊆V taki, że wszystkie wierzchołkiw G|U mają stopień większy lub równy k. Proszę
oszacować czas działania algorytmu.
Wrzucamy do kolejki wierchołki które na starcie mają stopień mniejszy od k, po kolei je usuwamy poprawiając stopnie
sąsiadów, jak któryś z nich stanie się mniejszy niż k to też go wrucamt do kolejki.
Złożoność czasowa: O(n^2)
"""


from queue import Queue


def k_degree(graph, k):
    n = len(graph)
    leave = [1 for _ in range(n)]
    degree = [len(graph[i]) for i in range(n)]
    queue = Queue()
    for i in range(n):
        if degree[i] < k:
            leave[i] = 0
            queue.put(i)
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if leave[v]:
                degree[v] -= 1
                if degree[v] < k:
                    leave[v] = 0
                    queue.put(v)
    for i in range(n):
        if leave[i]:
            print(i, end=" ")
