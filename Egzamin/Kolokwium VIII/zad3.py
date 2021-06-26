"""
Taki Dijkstra tylko mamy max_exp pól visited na każdy wierzchołek, więc f(i, j) = najkrótsza scieżka dotarcia do
wierzchołka i z co najamniej j punktów exp + sprawdzamy czy nie próbujemy przejść do już odwiedzonego wierzchołka
z większym expem (parent).
Złożoność czasowa: O(V^3 * max_exp^2)
"""


def get_index(shortest, visited):
    n = len(shortest)
    m = len(shortest[0])
    i_1, i_2 = None, None
    minimum = float('inf')
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and shortest[i][j] < minimum:
                minimum = shortest[i][j]
                i_1, i_2 = i, j
    return i_1, i_2


def look_for_parent(parent, curr_1, curr_2, check):
    if curr_1 == check:
        return False
    if curr_1 == -1:
        return True
    else:
        return look_for_parent(parent, parent[curr_1][curr_2][0], parent[curr_1][curr_2][1], check)


def adventure(G, P, s, m, max_exp):
    n = len(G)
    shortest = [[float('inf') for _ in range(max_exp + 1)] for _ in range(n)]
    visited = [[False for _ in range(max_exp + 1)] for _ in range(n)]
    parent = [[(-1, -1) for _ in range(max_exp + 1)] for _ in range(n)]
    shortest[m][0] = 0
    i, j = get_index(shortest, visited)
    while i is not None:
        visited[i][j] = True
        for k in range(1, n):
            if G[i][k] != 0:
                if j >= P[k][0] and not visited[k][(j + P[k][1]) % (max_exp + 1)] and look_for_parent(parent, i, j, k):
                    if shortest[i][j] + G[i][k] < shortest[k][(j + P[k][1]) % (max_exp + 1)]:
                        shortest[k][(j + P[k][1]) % (max_exp + 1)] = shortest[i][j] + G[i][k]
                        parent[k][(j + P[k][1]) % (max_exp + 1)] = (i, j)
        i, j = get_index(shortest, visited)
    minimum = float('inf')
    for l in range(max_exp):
        if minimum > shortest[s][l]:
            minimum = shortest[s][l]
    if minimum == float('inf'):
        return None
    return minimum


G_1 = [
        [0, 0, 12, 5, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 7, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0],
        [0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 3, 0, 2],
        [0, 4, 0, 0, 3, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
        [0, 0, 0, 0, 10, 0, 100, 0, 0, 0, 0],
        ]
P_1 = [(None, None), (2, 7), (0, 7), (0, 2), (4, 6), (2, 5), (10, 2), (15, 1), (15, 2), (6, 8), (15, 100)]
m_1, s_1, max_exp_1 = 0, 10, 20
odp_1 = 27  # 0, 3, 5, 4, 6, 10

G_2 = [
        [0, 1, 15, 0, 0, 0, 0, 2],
        [0, 0, 2, 0, 0, 0, 0, 1],
        [0, 0, 0, 3, 5, 0, 0, 10],
        [0, 0, 0, 0, 4, 0, 0, 5],
        [0, 0, 0, 0, 0, 13, 10, 12],
        [0, 0, 0, 0, 0, 0, 9, 11],
        [1, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0],
        ]
P_2 = [(None, None), (0, 7), (0, 1), (2, 4), (10, 1), (10, 15), (3, 7), (20, 5)]
m_2, s_2, max_exp_2 = 0, 7, 20
odp_2 = 26  # 0, 1, 2, 3, 4, 6, 7


G_3 = [
        [0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
P_3 = [(None, None), (0, 1), (0, 2), (0, 5), (1, 4), (2, 4), (5, 3), (5, 1), (4, 5), (2, 6), (1, 7), (10, 2)]
m_3, s_3, max_exp_3 = 0, 11, 30
odp_3 = 9  # 0, 2, 5, 9, 11


G_6 = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 100],
    [0, 0, 0, 0, 0],
    ]
P_6 = [(None, None), (0, 1), (0, 1), (0, 1), (3, 2)]
m_6, s_6, max_exp_6 = 0, 4, 10
odp_6 = 103  # 0, 1, 2, 3, 4


G_4 = [[0,1,0,100,0],
        [0,0,1,0,0],
        [1,0,0,0,0],
        [0,0,0,0,100],
        [0,0,0,0,0]]
P_4 = [(None,None),(0,1),(0,1),(9,100),(102,1000)]
m_4,s_4,max_exp_4 = 0,4,103
odp_4 = None


G_5 = [[0,1,0,100,0],
        [0,0,1,0,0],
        [1,0,0,0,0],
        [0,0,0,0,100],
        [0,0,0,0,0]]
P_5 = [(None,None),(0,1),(0,1),(2,100),(102,1000)]
m_5, s_5, max_exp_5 = 0,4,103
odp_5 = None


if __name__ == "__main__":
    tests = [[G_1, P_1, s_1, m_1, max_exp_1, odp_1], [G_2, P_2, s_2, m_2, max_exp_2, odp_2],
             [G_3, P_3, s_3, m_3, max_exp_3, odp_3], [G_4, P_4, s_4, m_4, max_exp_4, odp_4],
             [G_5, P_5, s_5, m_5, max_exp_5, odp_5], [G_6, P_6, s_6, m_6, max_exp_6, odp_6]]

    problem = False

    for i in range(len(tests)):
        G_t, P_t, s_t, m_t, max_exp_t, odp = tests[i]
        if odp == adventure(G_t, P_t, s_t, m_t, max_exp_t):
            print("Test", i + 1, "ok :)")
        else:
            print("Test", i + 1, "źle :(")
            problem = True

    if not problem:
        print("Wszystko ok, dobra robota <3")
