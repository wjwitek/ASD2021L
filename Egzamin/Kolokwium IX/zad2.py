"""
Tworzę graf skierowany w którym istnieje krawędź jeżeli z litery 1 do 2, jeżeli litera 1 jest przed literą 2. Przy czym
ponieważ jest to przechodznie to jak 3 jest po 2, to nie daje krawędzi jedynce.
Potem sprawdzam, czy graf jest dagiem i czy da się go jednoznacznie posortować topologicznie.
Złożoność czasowa: O(Vk + V^2), k - długość najdłuższego słowa
- implementacja tworzenia dagu jest źle! trzeba w "zbiorach" słów o tych samych początkacj porównywać
"""


def dfs_matrix(matrix):
    n = len(matrix)
    visited = [False for _ in range(n)]
    time = [-1 for _ in range(n)]
    timer = 0

    def visit(vertex):
        nonlocal timer
        visited[vertex] = True
        for i in range(n):
            if matrix[vertex][i] != 0 and not visited[i]:
                visit(i)
        time[vertex] = timer
        timer += 1

    for j in range(n):
        if not visited[j]:
            visit(j)

    return time


def topsort_matrix(matrix, used):
    n = len(matrix)
    visited = [False for _ in range(n)]
    result = []

    def visit(vertex):
        visited[vertex] = True
        for i in range(n):
            if not used[i]:
                continue
            if matrix[vertex][i] != 0 and not visited[i]:
                visit(i)
        result.append(vertex)

    for j in range(n):
        if not used[j]:
            continue
        if not visited[j]:
            visit(j)

    return result[::-1]


def pijany_mag(T):
    n = 26
    m = len(T)
    graph = [[0 for _ in range(n)] for _ in range(n)]
    used = [False for _ in range(n)]
    k = 1
    for i in range(m):
        if len(T[i]) > k:
            k = len(T[i])
    for i in range(m):
        for letter in T[i]:
            used[ord(letter) - ord('a')] = True
    for i in range(k):
        r = 0
        while r < m:
            while r < m and len(T[r]) <= i:
                r += 1
            if r == m:
                break
            q = r
            while q < m and len(T[q]) > i and T[q][i] == T[r][i]:
                q += 1
            if q < m and len(T[q]) > i and T[q][i] != T[r][i]:
                graph[ord(T[r][i]) - ord('a')][ord(T[q][i]) - ord('a')] = 1
            r = q
    # is it dag
    time = dfs_matrix(graph)
    for u in range(n):
        for v in range(n):
            if graph[u][v] == 1 and time[u] <= time[v]:
                return ""
    path = topsort_matrix(graph, used)
    if path is None:
        return ""
    result = ""
    for i in path:
        result += chr(i + 97)
    return result


T1 = ["wrt", "wrf", "er", "ett", "rftt"]
odp1 = 'wertf'

T2 = ['z', 'x']
odp2 = 'zx'

T3 = ['z', 'x', 'z']
odp3 = ''

tests = [(T1, odp1), (T2, odp2), (T3, odp3)]
for ind, (t, odp) in enumerate(tests):
    print('---------')
    print("test nr", ind)
    print("odpowiedz:", odp)
    a = pijany_mag(t)
    if a != odp:
        print(f"twoja odpowiedz: \"%s\"" % a)
        print("Błd w tescie")
    else:
        print("OK")



