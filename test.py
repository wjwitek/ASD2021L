from copy import deepcopy


def max_extending_path(G, s, t):
    from collections import deque

    def get_path(parent, res, t):
        if parent[t] == None:
            return res
        get_path(parent, res, parent[t])
        res.append(parent[t])
        return res

    def BFS(G, s, visited, val):
        deq = deque()
        visited[s] = True
        deq.append(s)
        while len(deq) != 0:
            u = deq.popleft()
            for i in range(len(G[u])):
                v = G[u][i][0]
                if visited[v] == False and G[u][i][1] >= val:
                    visited[v] = True
                    parent[v] = u
                    deq.append(v)
            visited[u] = True

    n = len(G)

    visited = [False] * n
    parent = [None] * n

    tmp = []
    # E
    for i in range(n):
        for j in range(len(G[i])):
            tmp.append(G[i][j][1])
    tmp.sort()  # ElogE

    # E
    tab = []
    i = 0
    curr = None
    while i < len(tmp):
        if curr != tmp[i]:
            tab.append(tmp[i])
            curr = tmp[i]
        i += 1

    i = 0
    j = len(tab) - 1
    mini = float('inf') * (-1)
    while (i < j):  # to jest log(e) wywołań BFS czyli log(e) wywołan V+E
        m = tab[(i + j) // 2]
        BFS(G, s, visited, m)
        if visited[t] == True:
            mini = max(mini, m)
            i = ((i + j) // 2) + 1
        else:
            j = ((i + j) // 2)
        for k in range(n):
            visited[k] = False
    res = get_path(parent, [], t)
    res.append(t)
    return res


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