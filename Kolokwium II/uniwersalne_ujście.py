"""
Mówimy,  że  wierzchołek t w  grafie  skierowanym  jest  uniwersalnym ujściem, jeśli
(a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz
(b) nie istnieje żadna krawędź wychodząca z t.
1.  Podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej (O(n2)).
2.  Pokazać, że ten problem można rozwiazac w czasie O(n) w reprezentacji macierzowej.
"""


def find_universal_n_2(matrix):
    n = len(matrix)
    visits = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                visits[j] += 1
    for i in range(n):
        if visits[i] == n - 1:
            flag = True
            for j in range(n):
                if matrix[i][j]:
                    flag = False
                    break
            if flag:
                return i
    return None


def is_sink(matrix, i):
    n = len(matrix)
    for j in range(n):
        if matrix[i][j]:
            return False
    for j in range(n):
        if not matrix[j][i]:
            return False
    return True


def find_universal_n(matrix):
    n = len(matrix)
    i = 0
    j = 1
    while i < n and j < n:
        if matrix[i][j]:
            i += 1
        else:
            j += 1
    if i >= n or is_sink(matrix, i):
        return -1
    else:
        return i
