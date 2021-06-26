"""
Redukuję graf do DAGu, usuwając niemożliwe przejścia i robię dynamik, gdzie f(i, j) oznacza maksymalną liczbę studentek
odiwedzonych kiedy docieram do i z j energii. Idę najpierw z pokoju profesora od studentek a potem w kolejnośći
malejących pokoi.
"""


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    k = 1
    while 6 * k - 1 < n:
        if n % (6 * k - 1) == 0:
            return False
        if n % (6 * k + 1) == 0:
            return False
        k += 1
    return True


def reduce_graph(G, T):
    n = len(G)
    graph = [[] for _ in range(n)]
    for i in range(n):
        if is_prime(i):
            for v, w in G[i]:
                if is_prime(v) and T[i] != T[v] and v < i:
                    graph[i].append([v, w])
    for v, w in G[0]:
        if is_prime(v):
            graph[0].append([v, w])
    return graph


def babiarz(G, T, W):
    n = len(G)
    graph = reduce_graph(G, T)
    students = [[-1 for _ in range(W + 1)] for _ in range(n)]
    for i, w in graph[0]:
        students[i][w] = 1
    maximum = 0
    for i in range(n - 1, -1, -1):
        for j in range(W + 1):
            if students[i][j] != -1:
                for k, w in graph[i]:
                    if j + w < W + 1 and students[i][j] + 1 > students[k][j + w]:
                        students[k][j + w] = students[i][j] + 1
                        if students[k][j + w] > maximum:
                            maximum = students[k][j + w]
    print(maximum)
    return maximum


G1 = [[(1,1),(2,5),(3,11),(4,3)],[(0,1),(3,3),(5,1),(6,1)],[(0,5),(3,3),(5,42)],[(2,3),(1,1),(0,11)],[(0,3)],[(2,42),(1,1)],[(1,1)]]
T1 = ["Łysy","Brun","Brun","Blond","Blond","Blond","Blond"]
W1 = 47
odp1 = [0,3,2]

G2 = [[(11,21),(8,15),(1,1),(2,5),(3,11),(4,3)],[(0,1),(3,3),(5,1),(6,1)],[(0,5),(3,3),(5,42)],[(2,3),(1,1),(0,11)],[(0,3)],[(2,42),(1,1)],[(1,1)],[(4,1),(8,10),(5,5)],[(0,15),(7,10)],[],[],[(0,21),(7,37)]]
T2 = ["Łysy","Brun","Blond","Brun","Blond","Blond","Brun","Brun","Blond","Brun","Brun","Blond"]
W2 = 63
odp2 = [0,11,7,5]

print(babiarz(G1,T1,W1) == odp1)
print(babiarz(G2,T2,W2) == odp2)
