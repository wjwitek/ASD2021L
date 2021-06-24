"""
Dijkstra, tylko z 6 polami visited/shortest oznaczającymi najtańszy koszt dotarcia na wyspę i za pomocą każdej
kombinacji poprzedniego środka transportu i kierunku jaki studiuje na tej wyspie.
Złożoność czasowa: O(n^2), gdzie n to liczba wysp
"""


def is_allowed(first, second):
    if first < 3 and second < 3:
        return False
    if first > 2 and second > 2:
        return False
    if first % 3 == second % 3:
        return False
    return True


def find_index(shortest, visited):
    n = len(shortest)
    best = float('inf')
    index_1, index_2 = None, None
    for i in range(n):
        for j in range(6):
            if shortest[i][j] < best and not visited[i][j]:
                best = shortest[i][j]
                index_1, index_2 = i, j
    return index_1, index_2


def evaluate(T, G, index_1, index_2, i, shortest, visited):
    if G[index_1][i] != 0:
        if T[i][0]:
            if G[index_1][i] == 5 and not visited[i][0] and is_allowed(index_2, 0) and shortest[index_1][index_2] + 5 < shortest[i][0]:
                shortest[i][0] = shortest[index_1][index_2] + 5
            elif G[index_1][i] == 7 and not visited[i][1] and is_allowed(index_2, 1) and shortest[index_1][index_2] + 7 < shortest[i][1]:
                shortest[i][1] = shortest[index_1][index_2] + 7
            elif G[index_1][i] == 11 and not visited[i][2] and is_allowed(index_2, 2) and shortest[index_1][index_2] + 11 < shortest[i][2]:
                shortest[i][2] = shortest[index_1][index_2] + 11
        if T[i][1]:
            if G[index_1][i] == 5 and not visited[i][3] and is_allowed(index_2, 3) and shortest[index_1][index_2] + 5 < shortest[i][3]:
                shortest[i][3] = shortest[index_1][index_2] + 5
            elif G[index_1][i] == 7 and not visited[i][4] and is_allowed(index_2, 4) and shortest[index_1][index_2] + 7 < shortest[i][4]:
                shortest[i][4] = shortest[index_1][index_2] + 7
            elif G[index_1][i] == 11 and not visited[i][5] and is_allowed(index_2, 5) and shortest[index_1][index_2] + 11 < shortest[i][5]:
                shortest[i][5] = shortest[index_1][index_2] + 11


def chodziarz(T, G, A, B):
    n = len(G)
    shortest = [[float('inf') for _ in range(6)] for _ in range(n)]
    visited = [[False for _ in range(6)] for _ in range(n)]
    # fly + inf = 0, ferry + inf = 1, bridge + inf = 2, fly + cer = 3, ferry + cer = 4, bridge + cer = 5
    if T[A][0]:
        for i in range(3):
            shortest[A][i] = 0
    if T[A][1]:
        for i in range(3, 6):
            shortest[A][i] = 0
    index_1, index_2 = find_index(shortest, visited)
    while index_1 is not None:
        for i in range(n):
            evaluate(T, G, index_1, index_2, i, shortest, visited)
        visited[index_1][index_2] = True
        index_1, index_2 = find_index(shortest, visited)
    return min(shortest[B])


T = [(True, False), (True, True), (False, True), (True, True), (True, False)]
G = [[0, 5, 5, 0, 11],
    [5, 0, 7, 11, 0],
    [5, 7, 0, 7, 5],
    [0, 11, 7, 0, 0],
    [11, 0, 5, 0, 0]]
print(chodziarz(T, G, 0, 4), "?=?", 28)
