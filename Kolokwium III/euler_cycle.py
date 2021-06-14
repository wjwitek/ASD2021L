"""
Dana jest struktura danych:
struct Edge{
int u, v; // u < v
Edge* next;
};
Napisz funkcje bool Euleran( Edge* E, int n ), która sprawdza czy graf zadany przez liste
krawedzi posiada cykl Eulera (n to liczba wierzchołków w grafie). Graf jest nieskierowany
i spójny. Krawedzie w liscie moga sie powtarzac. Funkcja powinna alokowac nie wiecej pamieci,
niz liniowo proporcjonalnie do ilosci krawedzi.
"""


def euler_cycle(edges, n):
    # create adjacency list
    graph = [[] for i in range(n)]
    for u, v in edges:
        if u not in graph[v]:
            graph[u].append(v)
            graph[v].append(u)
    # check condition for euler cycle
    for i in range(n):
        if len(graph[i]) % 2:
            return False
    return True
