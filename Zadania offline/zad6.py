"""
Weronika Witek
Implementacja funkcji z wykładu, z dodatkowym argumentem way, jest to tablica w której dla kaźdego elementu jest
zapisane pierwsze miasto po przeciwnej stronie, co pozwala na odtworzenie ścieżki jeśli zaczniemy od elementu n-1,
zapiszemy jako np. na dole to miasto i wszystkie miasta po way[n-1], następnie jako miasta na górze way[n - 1] i miasta
od wa[way[n-1]] + 1 do wa[n-1] itd., a więc uzupełniam raz ścieźkę górną, raz dolną i tablica way wskazuje kiedy należy
zmienić tablicę do której zapisujemy miasta.
Złożoność czasowa: O(n^2)
"""
from math import *

C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]


# simple function calculating euclidian distance between two points
def distance(first_x, first_y, second_x, second_y):
    return sqrt((first_x - second_x) ** 2 + (first_y - second_y) ** 2)


# implementation of function from lecture
def rec(i, j, bests, coordinates, way):
    if bests[i][j] < float('inf'):
        return bests[i][j]
    if i == j - 1:
        best = float('inf')
        best_index = -1
        for k in range(j - 1):
            temp = rec(k, j - 1, bests, coordinates, way) + distance(coordinates[k][1], coordinates[k][2],
                                                                     coordinates[j][1], coordinates[j][2])
            if best > temp:
                best = temp
                best_index = k
        bests[j - 1][j] = best
        way[i] = best_index  # way is always filled only for i, not j, that's why it's not filled in else below
    else:
        bests[i][j] = rec(i, j - 1, bests, coordinates, way) + distance(coordinates[j - 1][1], coordinates[j - 1][2],
                                                                        coordinates[j][1], coordinates[j][2])
    return bests[i][j]


def bitonicTSP(C):
    n = len(C)
    bests = [[float('inf')] * n for _ in range(n)]
    best = float('inf')
    C.sort(key=lambda x: x[1])
    bests[0][1] = distance(C[0][1], C[0][2], C[1][1], C[1][2])
    way = [-1] * n
    best_index = -1
    for i in range(n - 1):
        temp = rec(i, n - 1, bests, C, way) + distance(C[i][1], C[i][2], C[n - 1][1], C[n - 1][2])
        if best > temp:
            best = temp
            best_index = i
    # "decode" way, starting by filling array down and than switching each time index from way (k) is encountered
    way[n - 1] = best_index
    down = []
    up = []
    i = n - 1
    switch = True
    while i > 0:
        if switch:
            down.append(C[i][0])
            k = way[i]
            i -= 1
            while i > 0 and i > k:
                down.append(C[i][0])
                i -= 1
        else:
            up.append(C[i][0])
            k = way[i]
            i -= 1
            while i > 0 and i > k:
                up.append(C[i][0])
                i -= 1
        switch = not switch
    up.append(C[0][0])
    # print length of whole way
    # up must be printed from end, because it's filled by going from the end to beginning
    for i in range(len(up) - 1, -1, -1):
        print(up[i], end=" ")
    for city in down:
        print(city, end=" ")
    print(C[0][0])  # print starting city again
    print(best)


bitonicTSP(C)
