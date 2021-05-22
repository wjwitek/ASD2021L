from math import ceil


def partition(tab, p, r, median, flag=False):
    median_index = -1
    i = p - 1
    for j in range(p, r):
        if tab[j] < median:
            i += 1
            if tab[i] == median:
                median_index = j
            tab[i], tab[j] = tab[j], tab[i]
        elif tab[j] == median:
            median_index = j
    tab[i + 1], tab[median_index] = tab[median_index], tab[i + 1]
    return i + 1


def insertion_sort(array, start, end):
    for j in range(start, end):
        el = array[j]
        k = j - 1
        while el < array[k] and k > start - 1:
            array[k + 1] = array[k]
            array[k] = el
            k -= 1


def get_medians(array, p, r):
    # divide array into fives and choose median of each five
    j = p
    i = p  # i is index for array and k for medians
    while i + 4 < r:
        insertion_sort(array, i, i + 5)
        array[i + 2], array[j] = array[j], array[i + 2]
        i += 5
        j += 1
    # add remaining elements if n % 5 != 0
    if i < r:
        insertion_sort(array, i, r)
        array[i + (r - 1 - i) // 2], array[j] = array[j], array[i + (r - 1 - i) // 2]
        j += 1
    return j


def select(array, k, p, r, flag=False):
    # p is index of first element and r is index "after" last element
    while p <= r:
        index_after_medians = get_medians(array, p, r)
        # use select to find median of medians
        if index_after_medians - p == 1:
            median_of_medians = array[p]
        else:
            median_of_medians = select(array, (index_after_medians - p) // 2 + p, p, index_after_medians, True)
        current_index_of_median = partition(array, p, r, median_of_medians, flag)
        # either return kth element or decide in which part of array to search
        if current_index_of_median == k:
            return median_of_medians
        elif current_index_of_median > k:
            r = current_index_of_median
        else:
            p = current_index_of_median + 1

test = [0, 7, 10, 6, 8, 5, 9, 2, 1, 4, 3]
print(select(test, 7, 0, len(test)))
print(test)
