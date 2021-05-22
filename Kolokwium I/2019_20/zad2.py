from random import randint
"""
Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której podano wzrosty żołnierzy. Żołnierze zostaną
ustawieni na placu w szeregu malejąco względem wzrostu. Proszę zaimplementować funkcję: section(T,p,q) która zwróci
tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm powinien  być  możliwie  jak  najszybszy.
Proszę  w  rozwiązaniu  umieścić  1-2  zdaniowy  opis algorytmu oraz proszę oszacować jego złożoność czasową.
"""
"""
Assumption: positions in row of soldiers are counted from 0 (same as indexes in array)
Quick select on whole array is used to find soldier in position p and soldier on position q - p in array to right 
of soldier p. Because partition is used quick select moves all soldiers shorter than soldier p to their left and all 
soldiers higher than soldier q to their right.  
Average time complexity: O(n)
"""


def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] >= x:  # change -  should be sored from highest to smallest
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def randomized_partition(tab, p, r):
    i = randint(p, r)
    tab[r], tab[i] = tab[i], tab[r]
    return partition(tab, p, r)


def quick_select(tab, start, end, i):
    if start >= end:
        return tab[start]
    q = randomized_partition(tab, start, end)
    k = q - start + 1
    if k == i:
        return tab[q]
    elif i < k:
        return quick_select(tab, start, q - 1, i)
    else:
        return quick_select(tab, q + 1, end, i - k)


def section(array, p, q):
    n = len(array)
    p_value = quick_select(array, 0, n-1, p)
    q_value = quick_select(array, p+1, n-1, q-p)
    chosen_ones = [0] * (q - p + 1)
    k = 0
    for i in range(p, q + 1):
        chosen_ones[k] = array[i]
        k += 1
    return chosen_ones


test = [randint(160, 200) for _ in range(20)]
print(test)
print(section(test, 4, 9))
print(test)
