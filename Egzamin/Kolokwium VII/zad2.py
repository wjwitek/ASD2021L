"""
Na każdym przedmioce wykonujemy quickselect, aby znaleźć idelną ocenę i przechodzę po tablicy licząc ile jest ocen
pomiędzy oceną idelną, a oceną studentki.
Złożoność czasoa: O(n * m), gdzie n to liczba studentów, a m to liczba przedmiotów
"""
from random import randint
from copy import deepcopy


def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= x:
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


def calc_points(distance):
    if distance > 10:
        return 0
    return 10 - distance


def stypendia(T, A, k):
    new_array = deepcopy(T)
    m = len(T)
    n = len(T[0])
    points = 0
    for i in range(m):
        st_grade = new_array[i][A]
        best = quick_select(new_array[i], 0, n - 1, n - n // 4)
        difference = 0
        if st_grade == best:
            points += 10
        elif st_grade > best:
            for j in range(n):
                if st_grade > new_array[i][j] >= best:
                    difference += 1
        else:
            for j in range(n):
                if st_grade < new_array[i][j] <= best:
                    difference += 1
        points += calc_points(difference)
    if points >= k:
        return True
    return False



T = [[5.0, 5.0, 3.75, 4.5, 4.3, 4.1, 3.9, 4.9, 3.6, 2.0, 2.0, 2.0],
     [5.0, 4.6, 4.9, 4.2, 3.7, 4.0, 3.8, 4.01, 3.6, 3.5, 3.4, 2.0],
     [5.0, 4.7, 3.0, 3.5, 2.8, 2.7, 2.5, 2.0, 2.3, 2.2, 2.1, 2.4]]
print(stypendia(T,7,19) == True)
print(stypendia(T,7,21) == False)


