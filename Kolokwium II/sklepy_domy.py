"""
W miasteczku są sklepy i domy. Trzeba sprawdzić jak daleko do najbliższego sklepu mająmieszkańcy.
struct Vertex{
    bool shop; // true-sklep, false-dom
    int* distances; // tablica odległości do innych wierzchołków
    int* edges; // numery wierzchołków opisanych w distances
    int edge; // rozmiar tablicy distances (i edges)
    int dstore; // odległość do najbliższego sklepu};
Zaimplementować funkcję distanceToClosestStore(int n, Vertex* village) uzupełniającą dstore dla tablicy Vertexów i
oszacować złożoność algorytmu.
BFS z każdego sklepu, ale kończący się na domach które mają już bliższy sklep i sklepach
Zakładam, że dostajemy tablicę wierzchołków.
"""


from queue import Queue


class Vertex:
    def __init__(self):
        self.shop = False
        self.distance = []
        self.edges = []
        self.dstore = float('inf')


def BFS(start, village):
    q = Queue()
    n = len(village)
    visited = [False for _ in range(n)]
    start.dstore = 0
    q.put(start)
    while not q.empty():
        u = q.get()
        for i in range(len(u.distance)):
            if not visited[u.edges[i]] and not village[u.edges[i]].shop \
                    and u.dstore + u.distance[i] < village[u.edges[i]].dstore:
                village[u.edges[i]].dstore = u.dstore + u.distance[i]
                q.put(village[u.edges[i]])


def get_dstore(village):
    for i in range(len(village)):
        if village[i].shop:
            BFS(village[i], village)
