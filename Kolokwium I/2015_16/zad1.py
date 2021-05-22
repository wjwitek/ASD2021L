from random import randint
"""
Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta
przyjmuje na wejściu dwie n2-elementowe tablice (A i B) i zapisuje w tablicy B taką permutację
elementów z A, że:n−1∑i=0B[i]¬2n−1∑i=nB[i]¬...¬n2−1∑i=n2−nB[i]. Proszę zaimplementować funkcję SumSort
tak, by działała możliwie jak najszybciej. Proszę oszacować i podać jej złożoność czasową.
"""
# Time complexity: O(n^2) - time it takes to calculate sums and write elements to B


def calculate_sums(array_a, array_b, n):
    # calculate sums in ranges n * i to n * (i + 1) - 1 adding indexes of where they start
    for i in range(n):
        partial_sum = 0
        for j in range(n):
            partial_sum += array_a[n * i + j]
        array_b[n ** 2 - 1 - i] = (partial_sum, n * i)


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


def rewrite(array_a, array_b, n):
    k = 0
    for i in range(n):
        starting_index = array_b[n**2-n+i][1]
        for j in range(n):
            array_b[k] = array_a[starting_index + j]
            k += 1


def sum_sort(array_a, array_b, n):
    calculate_sums(array_a, array_b, n)
    print(array_b)
    quicker_sort(array_b, n**2-n, n**2-1, 0)
    rewrite(array_a, array_b, n)


m = 4
my_a = [randint(1, 100) for _ in range(m ** 2)]
my_b = [0] * m ** 2
sum_sort(my_a, my_b, m)
print(my_a)
print(my_b)
