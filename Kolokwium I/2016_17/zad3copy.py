"""
Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy
jest sumą dwóch innych liczb z tablicy. Zaproponowany algorytm powinien być możliwie jak najszybszy.
Proszę oszacować jego złożoność obliczeniową.
"""


def quicker_partition(tab, p, r):
    x = tab[r]
    i = p - 1
    k = r - 1
    j = p
    while j <= k:
        if tab[j] < x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
            j += 1
        elif tab[j] == x:
            tab[k], tab[j] = tab[j], tab[k]
            k -= 1
        else:
            j += 1
    for l in range(r - k):
        tab[l + i + 1], tab[k + 1 + l] = tab[k + 1 + l], tab[l + i + 1]
    return i, i + r - k + 1


def quicker_sort(tab, p, r):
    while p < r:
        left, right = quicker_partition(tab, p, r)
        if left - p < r - right:
            quicker_sort(tab, p, left)
            p = right
        else:
            quicker_sort(tab, right, r)
            r = left


def binary_search(array, p, r, key):
    if p <= r:
        middle = p + (r - p) // 2
        if array[middle] == key:
            return middle
        elif array[middle] > key:
            return binary_search(array, p, middle - 1, key)
        else:
            return binary_search(array, middle + 1, r, key)
    return -1


def check(array):
    n = len(array)
    # create array of all possible sums
    sums = [0] * ((n**2 - n) // 2)
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            sums[k] = array[i] + array[j]
            k += 1
    # sort sums
    quicker_sort(sums, 0, len(sums) - 1)
    # check each element of array for same value in sums (binary search)
    for i in range(len(array)):
        if binary_search(sums, 0, len(sums) - 1, array[i]) == -1:
            return False
    return True


test = [-5, -3, -2, 1, 2, 3, 5, 100]
test_2 = [-5, -3, -2, 2, 3, 5]
print(check(test))
