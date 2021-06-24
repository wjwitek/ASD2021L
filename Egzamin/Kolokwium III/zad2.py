"""
Sortuje przedziały rosnąco, tak, że w pierwszej kolejności są posortowane po początkach, a w drugiej po końcach.
Następnie przechodzą po przedziałach, trzymając dotychczas znaleziony najdłuższy podprzdział, i sprawdzam, czy spośród
tych z którymi się łączy nie jest coś większe, a sprawdzeniu wszystkich przedziałów łączących się z aktualnym,
przechodzę do ostatniego z któym porównywałam (korzystam tutaj z tego, że w żadnym miejscu nie przecinają się więcej niż
dwa przedziały - dzięki temu jest samo przejsćie liniowe). Jak z niczym się nie przecin, to po prostu idę do następnego.
Złożoność czasowa: O(nlogn)
"""


def quicker_partition(tab, p, r, idx):
    x = tab[r][idx]
    i = p - 1
    k = r - 1
    j = p
    while j <= k:
        if tab[j][idx] < x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
            j += 1
        elif tab[j][idx] == x:
            tab[k], tab[j] = tab[j], tab[k]
            k -= 1
        else:
            j += 1
    for l in range(r - k):
        tab[l + i + 1], tab[k + 1 + l] = tab[k + 1 + l], tab[l + i + 1]
    return i, i + r - k + 1


def quicker_sort(tab, p, r, idx):
    while p < r:
        left, right = quicker_partition(tab, p, r, idx)
        if left - p < r - right:
            quicker_sort(tab, p, left, idx)
            p = right
        else:
            quicker_sort(tab, right, r, idx)
            r = left


def intervals(T):
    n = len(T)
    quicker_sort(T, 0, n - 1, 1)
    quicker_sort(T, 0, n - 1, 0)
    index = 0
    second = 1
    best = 0
    i, j = None, None
    while index < n - 1:
        while second < n and T[second][0] < T[index][1]:
            if T[second][1] > T[index][1] and T[index][1] - T[second][0] > best:
                best = T[index][1] - T[second][0]
                i = T[second][0]
                j = T[index][1]
            elif T[second][1] <= T[index][1] and T[second][1] - T[second][0] > best:
                best = T[second][1] - T[second][0]
                i = T[second][0]
                j = T[second][1]
            second += 1
        if index == second - 1:
            index += 1
            second += 1
        else:
            index = second - 1
            second = index + 1
    return i, j



T = [(1,5),(1,3),(4,6),(7,8),(8,10),(12,15)]
print(intervals(T),(1,3))
T = [(10,11),(9,10),(8,9),(1,2),(2,3),(6,7),(1,3),(11,15),(12,15)]
print(intervals(T),(12,15))
T = [(0,10),(1,3),(3,7),(7,11),(10,11)]
print(intervals(T),(3,7))
