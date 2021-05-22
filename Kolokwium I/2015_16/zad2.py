"""
Dana jest n elementowa tablica A zawierająca liczby naturalne (potencjalnie bardzo duże).
Wiadomo, że tablica A powstała w dwóch krokach. Najpierw wygenerowano losowo (z nieznanym rozkładem)
n różnych liczb nieparzystych i posortowano je rosnąco. Następnie wybrano losowo ceil(logn) elementów powstałej tablicy
i zamieniono je na losowo wybrane liczby parzyste. Proszę zaproponować (bez implementacji!) algorytm sortowania tak
powstałych danych. Algorytm powinien być możliwie jak najszybszy. Proszę oszacować i podać jego złożoność czasową.
"""


# sort list with even numbers and merge it with list of odd numbers
def put_even_at_the_end(array):
    n = len(array)
    i = k = 0
    while True:
        if array[i] % 2 == 1:
            i += 1
        else:
            if k < i:
                k += 1
            while k < n and array[k] % 2 == 0:
                k += 1
            if k == n:
                return i
            array[i], array[k] = array[k], array[i]


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


def merge(array, start_1, end_1, start_2, end_2, temp):
    starter = start_1
    i = 0
    while start_1 <= end_1 and start_2 <= end_2:
        if array[start_1] < array[start_2]:
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


def sort_odd_even(array):
    index = put_even_at_the_end(array)
    quicker_sort(array, index, len(array) - 1)
    merge(array, 0, index - 1, index, len(array) - 1, [0] * len(array))


test = [1, 4, 1, 3, 8, 6, 8, 4, 3, 3, 3, 10]
sort_odd_even(test)
print(test)
