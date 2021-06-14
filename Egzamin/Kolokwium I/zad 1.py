"""
Dla każdej liczby w tablicy obliczam jej logrytm o podstawie a (dla a > 1, logarytm jest funkcją rosnącą, więc
zachowuje kolejność w liście) i za pomocą wykładników sortuje liczby przy użyciu bucekt sort.
Złożoność czasowa: O(n)
"""
from zad1testy import runtests
import math


def insertion_sort_array(list_to_sort, idx):
    n = len(list_to_sort)
    for i in range(n):
        el = list_to_sort[i]
        k = i - 1
        while el[idx] < list_to_sort[k][idx] and k > - 1:
            list_to_sort[k + 1] = list_to_sort[k]
            list_to_sort[k] = el
            k -= 1


# bucket sort from 0 to 1
def bucket_sort(tab, idx):
    n = len(tab)
    bucket = [[] for _ in range(n)]
    for num in tab:
        if num[idx] == 1:
            bucket[n - 1].append(num)
            continue
        bucket[int(num[idx] * n)].append(num)
    for i in range(n):
        insertion_sort_array(bucket[i], idx)
    index = 0
    for i in range(n):
        for el in bucket[i]:
            tab[index] = el
            index += 1


def fast_sort(tab, a):
    n = len(tab)
    # add to tab logarithms of tab[i]
    for i in range(n):
        tab[i] = [math.log(tab[i], a), tab[i]]
    # sort array by logarithms
    bucket_sort(tab, 0)
    # remove logarithms from tab
    for i in range(n):
        tab[i] = tab[i][1]
    return tab


runtests(fast_sort)