"""
Weronika Witek
f(i) - maksymalna przepustowość ścieżki z s do i
f(i) - max po (i, j){min{c(i, j), f(j)}}
Modyfikacja algorytmu Dijsktry:
- zamiast najmniejszych odległości dla wierzchołka, mamy maksymalną przepustowość (f(i))
- początkowo te przepustowości wszędzie mają wartość 0, poza źródłem, gdzie mają wartość inf
- za każdym razem z kolejki wyciągamy wierzchołek o maksymalnym priorytecie, a nie minimalnym
Złożoność czasowa: O(ElogV)
"""
from copy import deepcopy


class PriorityQueueMax:
    def __init__(self):
        self.heap = []
        self.size = 0

    def heapify(self, i):
        if i * 2 + 1 < self.size and self.heap[i * 2 + 1][0] > self.heap[i][0]:
            largest = i * 2 + 1
        else:
            largest = i
        if (i + 1) * 2 < self.size and self.heap[(i + 1) * 2][0] > self.heap[largest][0]:
            largest = (i + 1) * 2
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def get(self):
        if self.size < 1:
            print("Cannot take from empty heap.")
            exit(1)
        maximum = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()
        self.heapify(0)
        return maximum

    def put(self, key):
        self.size += 1
        self.heap.append(key)
        i = self.size - 1
        while i > 0 and self.heap[(i - 1) // 2][0] < self.heap[i][0]:
            self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i - 1) // 2]
            i = (i - 1) // 2

    def empty(self):
        if self.size == 0:
            return True
        return False


def max_extending_path(G, s, t):
    n = len(G)
    capacity = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    capacity[s] = float('inf')
    queue = PriorityQueueMax()
    queue.put((float('inf'), s))
    while not queue.empty():
        p, u = queue.get()
        for v, w in G[u]:
            temp = min(w, p)
            if temp > capacity[v]:
                capacity[v] = temp
                parent[v] = u
                queue.put((temp, v))
    if parent[t] is None:
        return []
    result = [t]
    while parent[t] is not None:
        result.append(parent[t])
        t = parent[t]
    return result[::-1]


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1, 4), (2, 3)],  # 0
     [(3, 2)],  # 1
     [(3, 5)],  # 2
     []]  # 3
s = 0
t = 3
C = 3

GG = deepcopy(G)
path = max_extending_path(GG, s, t)

print("Sciezka :", path)

if path == []:
    print("Błąd (1): Spodziewano się ścieżki!")
    exit(0)

if path[0] != s or path[-1] != t:
    print("Błąd (2): Zły początek lub koniec!")
    exit(0)

capacity = float("inf")
u = path[0]

for v in path[1:]:
    connected = False
    for (x, c) in G[u]:
        if x == v:
            capacity = min(capacity, c)
            connected = True
    if not connected:
        print("Błąd (3): Brak krawędzi ", (u, v))
        exit(0)
    u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
    print("Błąd (4): Niezgodna pojemność")
else:
    print("OK")
