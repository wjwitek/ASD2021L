"""
Zakładam, że kopuły nie mogą wykraczać poza park.
f(i) - minimalny koszt pokrycia kopułami do punktu bi
Złożoność czasowa: O(nlogn)
"""


from zad2testy import runtests
from Inne.binary_search import binary_search


def pokrycie(P, prz):
    a_min, b_max = prz
    n = len(P)
    P.sort(key=lambda x: x[1])
    f = [-1 for _ in range(n)]
    index = 0
    while index < n:
        a, b, c = P[index]
        if a < a_min or b > b_max:
            index += 1
            continue
        if a == a_min and (f[index] == -1 or f[index] > c):
            f[index] = c
        else:
            left, right = binary_search(P, 1, a, 0, index)
            for k in range(left + 1, right):
                if f[k] != -1 and (f[index] == -1 or f[index] > f[k] + c):
                    f[index] = f[k] + c
        index += 1
    cheapest = -1
    left, right = binary_search(P, 1, b_max, 0, n - 1)
    for k in range(left + 1, right):
        if f[k] != -1 and (cheapest == -1 or f[k] < cheapest):
            cheapest = f[k]
    return cheapest


runtests(pokrycie)
