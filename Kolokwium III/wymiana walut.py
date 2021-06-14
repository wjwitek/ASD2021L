"""
Na tablicach w kantorze wisi lista trójek (waluta1, waluta2, kurs). Każda z takich trójek oznacza, że kantor kupi n
waluty2 za kurs*n waluty1.
a) Znajdź najkorzystniejszą sekwencję wymiany waluty A na walutę B
b) Czy istnieje taka sekwencja wymiany walut, która zaczyna się i kończy w tej samej walucie i kończymy z większą
ilością pieniędzy niż zaczynaliśmy?
Tworzymy graf skierowany, w którym krawędzie idą od waluty1 do waluty2 i mają wagę kurs. Następnie logarytmujemy
wagi krawędzi i za pomocą algorytmu Bellmana-Forda szukamy najkrótszej ścieżki z A do B. Można się wzbogacić na
wymianie walut jeśli w grafie istnieje ujemny cykl.
"""
from math import log


def cheapest_exchange(currency, n, A, B):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for u, v, value in currency:
        graph[u][v] = currency
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                graph[i][j] = log(graph[i][j])
    shortest = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    shortest[A] = 0
    for i in range(n):
        for u, v, value in currency:
            if shortest[v] > shortest[u] + value:
                shortest[v] = shortest[u] + value
                parent[v] = u
    # recreate sequence of exchange
    result = [B]
    while parent[B] is not None:
        result.append(parent[B])
        B = parent[B]
    # look for negative cycle
    for u, v, value in currency:
        if not shortest[v] <= shortest[u] + value:
            return result, True
    return result, False
