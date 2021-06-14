"""
Zaproponuj algorytm, który policzy ile jest najkrótszych sciezek w grafie z danego wierzchołka
u do v. Wskazówka: Dla kazdej najkrótszej sciezki przechodzacej przez wierzchołek w,
odległosc w od startu jest taka sama jak odległosc w do mety.
Pomysł: Dijkstra z dodatkową tablicą counter, która zapisuje liczbę najkrótszych ścieżek do x. Nie musimy się
martwić, że po zmianie countera trzeba by poprawić scieżki będące dziećmi punktu, bo wszystkie najkrótsze ścieżki
dochodzące do tego punktu będą rozważone wcześniej.
Złożoność czasowa: O(ElogV) lub O(V^2) - zależy od reprezentacji macierzy, ja przyjmuje listową
"""
from queue import PriorityQueue


def count_shortest_paths(graph, u, v):
    n = len(graph)
    shortest = [float('inf') for _ in range(n)]
    counter = [0 for _ in range(n)]
    shortest[u] = 0
    queue = PriorityQueue()
    queue.put((0, u))
    while not queue.empty():
        p, w = queue.get()
        if p > shortest[w]:
            continue
        for node, weight in graph[w]:
            if p + weight < shortest[node]:
                shortest[node] = p + weight
                counter[node] = 1
                queue.put((shortest[node], node))
            elif p + weight == shortest[node]:
                counter[node] += 1
    return counter[v]
