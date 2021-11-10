"""
Weronika Witek
Sortuje przedziały po początkach.
f(i, j) = początek i koniec największego przecięcia zawierającego j przedziałów, w tym i-ty przedział i j-1 poprzednich
Złożoność czasowa: O(n^2k)
Złożoność pamięciowa: O(n^2)
"""

from zad3testy import runtests


def kintesect(A, k):
    n = len(A)
    A = [[A[i][0], A[i][1], i] for i in range(n)]
    A.sort()
    arr = [[(-1, -1) for _ in range(k + 1)] for _ in range(n)]
    parent = [[(-1, -1) for _ in range(k + 1)] for _ in range(n)]
    for i in range(n):
        arr[i][1] = (A[i][0], A[i][1])
    # calculate f
    for i in range(n):
        for j in range(1, k):
            if arr[i][j][0] == -1:
                continue
            l = i + 1
            while l < n and A[l][0] < arr[i][j][1]:
                if A[l][1] >= arr[i][j][1] and A[l][0] <= arr[i][j][0]:
                    if arr[l][j + 1][0] == -1:
                        arr[l][j + 1] = arr[i][j]
                        parent[l][j + 1] = (i, j)
                    elif arr[l][j + 1][1] - arr[l][j + 1][0] < arr[i][j][1] - arr[i][j][0]:
                        arr[l][j + 1] = arr[i][j]
                        parent[l][j + 1] = (i, j)
                elif A[l][0] <= arr[i][j][0] and A[l][1] >= arr[i][j][1]:
                    if arr[l][j + 1][0] == -1:
                        arr[l][j + 1] = (arr[i][j][0], A[l][1])
                        parent[l][j + 1] = (i, j)
                    elif arr[l][j + 1][1] - arr[l][j + 1][0] < A[l][1] - arr[i][j][0]:
                        arr[l][j + 1] = (arr[i][j][0], A[l][1])
                        parent[l][j + 1] = (i, j)
                elif A[l][1] >= arr[i][j][1] and A[l][0] > arr[i][j][0]:
                    if arr[l][j + 1][0] == -1:
                        arr[l][j + 1] = (A[l][0], arr[i][j][1])
                        parent[l][j + 1] = (i, j)
                    elif arr[l][j + 1][1] - arr[l][j + 1][0] < arr[i][j][1] - A[l][0]:
                        arr[l][j + 1] = (A[l][0], arr[i][j][1])
                        parent[l][j + 1] = (i, j)
                else:
                    if arr[l][j + 1][0] == -1:
                        arr[l][j + 1] = (A[l][0], A[l][1])
                        parent[l][j + 1] = (i, j)
                    elif arr[l][j + 1][1] - arr[l][j + 1][0] < A[l][1] - A[l][0]:
                        arr[l][j + 1] = (A[l][0], A[l][1])
                        parent[l][j + 1] = (i, j)
                l += 1
    # recreate result based in parent
    best = 0
    for i in range(n):
        if arr[i][k][1] - arr[i][k][0] > arr[best][k][1] - arr[best][k][0]:
            best = i
    index = k
    result = []
    while best != -1:
        result.append(A[best][2])
        best, index = parent[best][index]
    return result


runtests(kintesect)
