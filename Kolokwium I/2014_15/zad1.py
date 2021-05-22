"""
Napisać funkcję: void sortString(string A[]);Funkcja sortuje tablicę n stringów różnej długości.
Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.
"""


# sorts strings from longest to shortest
def quicker_partition(tab, p, r):
    x = len(tab[r])
    i = p - 1
    k = r - 1
    j = p
    while j <= k:
        if len(tab[j]) > x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
            j += 1
        elif len(tab[j]) == x:
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
            quicker_sort(tab, right, r)
            r = left
        else:
            quicker_sort(tab, p, left)
            p = right


def count_sort(array, idx):
    k = 25
    counts = [0] * (k + 1)
    sorted_array = [0] * len(array)
    for i in range(len(array)):
        if idx < len(array[i]):
            counts[ord(array[i][idx]) - ord('a')] += 1
        else:
            counts[0] += 1
    for i in range(1, k + 1):
        counts[i] = counts[i] + counts[i - 1]
    for i in range(k + 1):
        counts[i] -= 1
    for i in range(len(array) - 1, -1, -1):
        if idx < len(array[i]):
            sorted_array[counts[ord(array[i][idx]) - ord('a')]] = array[i]
            counts[ord(array[i][idx]) - ord('a')] -= 1
        else:
            sorted_array[counts[0]] = array[i]
            counts[0] -= 1
    for i in range(len(sorted_array)):
        array[i] = sorted_array[i]


def sort_string(array):
    quicker_sort(array, 0, len(array) - 1)
    index = len(array[0])
    end = 1
    while end <= len(array):
        # move to last string of length at least index
        while end < len(array) and len(array[end]) >= index:
            end += 1
        # decide by which index to sort
        if end == len(array):
            print(array, 0)
            count_sort(array, 0)
            return
        index = len(array[end])
        print(array, index)
        count_sort(array, index)


test = ["abba", "z", "b", "x", "c", "cba", "aaa", "aza", "aab", "aaaaaaaaaaaaaaaa"]
sort_string(test)
print(test)
