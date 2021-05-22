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


def check(array):
    n = len(array)
    quicker_sort(array, 0, n - 1)
    for i in range(n):
        j, k = 0, n - 1
        not_found = True
        while j < k:
            if j == i:
                i += 1
                continue
            if k == i:
                k -= 1
                continue
            if array[j] + array[k] == array[i]:
                not_found = False
                break
            elif array[j] + array[k] < array[i]:
                j += 1
            else:
                k -= 1
        if not_found:
            return False
    return True


test = [-5, -3, -2, 1, 2, 3, 5]
test_2 = [0, 1]
print(check(test))
# time complexity: n^2
