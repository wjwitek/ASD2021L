#złożoność czasowa O(E*3*2log(V))
#zł pamięciowa O(E)
#Ogólna idea:
#tworzymy "wiekszy graf" trójwymiarowy o stróktórze distances : d[wierzchołek][kierunek][dotarłem uzywając tego śrdoka transportu]
#puszczamy djikstrę z narzuconymi przez treść zadania ograniczeniami 



from queue import PriorityQueue


def cost_index(w):
    if w == 5:
        return 0
    if w == 7:
        return 1
    if w == 11:
        return 2

def build_graph(G):
    n = len(G)
    H = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                H[u].append([v, G[u][v]])
    return H


def chodziarz(T,G,A,B):
    n = len(G)
    Q = PriorityQueue()
    G = build_graph(G)
    d = [[[float("inf") for _ in range(3)] for _ in range(2)] for _ in range(n)]
    visited = [[[False for _ in range(3)] for _ in range(2)] for _ in range(n)]

    for j in range(3):
        for i in range(2):
            if T[A][i] == True:
                d[A][i][j] = 0
                Q.put((0, A, j, i))

    while not Q.empty():
        _, u, t, facU = Q.get()
        if not visited[u][facU][t]:
            visited[u][facU][t] = True
            for v, w in G[u]:
                facV = (facU + 1)%2
                if T[v][facV] and cost_index(w) != t and d[v][facV][cost_index(w)] > d[u][facU][t] + w:
                    d[v][facV][cost_index(w)] = d[u][facU][t] + w
                    Q.put((d[v][facV][cost_index(w)], v, cost_index(w),facV))

    _min = float("inf")
    for i in range(2):
        _min = min(_min,min(d[B][i]))
    return _min


T = [(True,False),(True,True),(False,True),(True,True),(True,False)]
G =[[0, 5, 5, 0, 11],
    [5, 0, 7, 11, 0],
    [5, 7, 0, 7, 5],
    [0, 11, 7, 0, 0],
    [11, 0, 5, 0, 0]]
print(chodziarz(T,G,0,4),"?=?",10)