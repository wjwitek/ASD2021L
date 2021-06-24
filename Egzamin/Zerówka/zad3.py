"""
Zmodyfikowany algorytm Dijkstry z dwoma polami visited na każdy wierzchołek - jedno oznacza najmniejszy koszt dotarcia
do wierzchołka tak, że ostatni krok to były dwumilowe buty, a jedno tak, że ostatni krok był normalny, gdy robimy krok
dwumilowymi butami to traktujemy to tak, jakby wierzchołka po drodze nie było i nie zaznaczamy mu visited itp.
Złożoność czasowa: O(V^3)
Złożoność pamięciowa: O(v)
"""
from zad3testy import runtests


def find_shortest(shortest, visited):
    n = len(shortest)
    best_value = float('inf')
    best_index, past = None, None
    for i in range(n):
        for j in range(2):
            if not visited[i][j] and shortest[i][j] < best_value:
                best_value = shortest[i][j]
                best_index = i
                past = j
    return best_index, past


def jumper(G, s, w):
    n = len(G)
    # 0 - last step with boots, 1 - last step without boots
    shortest = [[float('inf') for _ in range(2)] for _ in range(n)]
    visited = [[False for _ in range(2)] for _ in range(n)]
    shortest[s][1] = 0
    index, past = find_shortest(shortest, visited)
    visited[s][1] = True
    visited[s][0] = True
    shortest[s][0] = 0
    while index is not None:
        if past == 1:
            for i in range(n):
                if G[index][i]:
                    for j in range(n):
                        if j == index:
                            continue
                        if G[i][j] and max(G[index][i], G[i][j]) + shortest[index][past] < shortest[j][0]:
                            shortest[j][0] = max(G[index][i], G[i][j]) + shortest[index][past]
        for i in range(n):
            if G[index][i] and G[index][i] + shortest[index][past] < shortest[i][1]:
                shortest[i][1] = G[index][i] + shortest[index][past]
        visited[index][past] = True
        index, past = find_shortest(shortest, visited)
    for row in shortest:
        print(row)
    return min(shortest[w])




runtests(jumper)