"""
Weronika Witek
Tworzę nową tablicę, która zawiera krotki postaci (wartość, indeks w tablicy wejściowej). Tak powstają tablicę
sortuje stabilnie po wartościach (żeby dla jednakowych elementów przesunięcie było minimalne) i sprawdzam największą
różnicę między indeksem w tablicy wejściowej a obecnym.
Złożoność czasowa: O(nlogn)
Złożoność pamięciowa: O(n)
"""
from zad1testy import runtests


def merge(array, start_1, end_1, start_2, end_2, temp, idx):
    starter = start_1
    i = 0
    while start_1 <= end_1 and start_2 <= end_2:
        if array[start_1][idx] <= array[start_2][idx]:
            temp[i] = array[start_1]
            start_1 += 1
        else:
            temp[i] = array[start_2]
            start_2 += 1
        i += 1
    # add elements remaining
    while start_1 <= end_1:
        temp[i] = array[start_1]
        i += 1
        start_1 += 1
    while start_2 <= end_2:
        temp[i] = array[start_2]
        i += 1
        start_2 += 1
    # take elements from temp and put them back in array
    for j in range(i):
        array[j + starter] = temp[j]


def merge_sort(array_to_sort, idx):
    temp = [0] * len(array_to_sort)

    def merge_sort_recursion(array, p, r, idx):
        if p < r:
            middle = (p + r) // 2
            merge_sort_recursion(array, p, middle, idx)
            merge_sort_recursion(array, middle + 1, r, idx)
            merge(array, p, middle, middle + 1, r, temp, idx)

    merge_sort_recursion(array_to_sort, 0, len(array_to_sort) - 1, idx)


def chaos_index(T):
    n = len(T)
    copy = [(T[i], i) for i in range(n)]
    merge_sort(copy, 0)
    minimum = 0
    for i in range(n):
        if abs(copy[i][1] - i) > minimum:
            minimum = abs(copy[i][1] - i)
    return minimum


runtests( chaos_index )
