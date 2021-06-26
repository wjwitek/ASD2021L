"""
Bellman-Ford tylko z ograniczeniem na tą liczbę czerwnoych kart (distance tablica 2D).
Złożoność czasowa: O(x * V^3)
"""


def bellman_ford_matrix(graph, source, x, colors):
    n = len(graph)
    distance = [[float('inf') for _ in range(x + 1)] for _ in range(n)]
    parent = [[(-1, -1) for _ in range(x + 1)] for _ in range(n)]
    for i in range(x + 1):
        distance[source][i] = 0
    # calculate distances
    for k in range(n - 1):
        for i in range(n):
            if colors[i] == "niebieski":
                continue
            for j in range(n):
                if colors[j] == "niebieski":
                    continue
                if graph[i][j] != 0:
                    if colors[i] == "czerwony" and colors[j] == "czerwony":
                        for s in range(x):
                            if distance[j][s + 1] > distance[i][s] + graph[i][j]:
                                distance[j][s + 1] = distance[i][s] + graph[i][j]
                                parent[j][s + 1] = (i, s)
                    elif colors[i] == "czerwony":
                        for s in range(x):
                            if distance[j][0] > distance[i][s] + graph[i][j]:
                                distance[j][0] = distance[i][s] + graph[i][j]
                                parent[j][0] = (i, s)
                    else:
                        if distance[j][0] > distance[i][0] + graph[i][j]:
                            distance[j][0] = distance[i][0] + graph[i][j]
                            parent[j][0] = (i, 0)
    return distance, parent


def mlodszy_pasjonat(M, A, B, y, D, x, T):
    distance, parent = bellman_ford_matrix(M, A, x, T)
    best_index = 0
    for s in range(1, x + 1):
        if distance[B][s] < distance[B][best_index]:
            best_index = s
    # recreate path
    result = []
    curr = B
    while curr != -1:
        result.append(curr)
        curr, best_index = parent[curr][best_index]
    return result[::-1]


from copy import deepcopy
M = [[0,10,0,120,0,0,1],
      [10,0,6,0,0,0,0],
      [0,6,0,7,0,0,0],
      [120,0,7,0,1,0,0],
      [0,0,0,1,0,1,0],
      [0,0,0,0,1,0,1],
      [1,0,0,0,0,1,0]]
T = ["biały","biały","czerwony","czarny","czerwony","czerwony","biały"]

A = 0
B = 3
y = 6
D = 4
x = 0
odp = [0,3]
print(mlodszy_pasjonat(deepcopy(M),A,B,y,D,x,deepcopy(T)), odp)

y = 8
x = 1
odp = [0,1,2,3]
print(mlodszy_pasjonat(deepcopy(M),A,B,y,D,x,deepcopy(T)), odp)

y = 10
x = 3
odp = [0,6,5,4,3]
print(mlodszy_pasjonat(deepcopy(M),A,B,y,D,x,deepcopy(T)), odp)

