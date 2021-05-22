from countsort import counting_sort_idx
from math import ceil
from math import log2
from random import randint


# algorithm to sort array of n elements in range (0, n**2-1)
# first represent each number in base n (now they will have to digits, stored in tuple each)
# second use count sort twice (for second, than fist digit)
# convert numbers back to original
def convert_to_n(array, base):
    for i in range(len(array)):
        value = array[i]
        array[i] = (value // base, value % base)


def convert_back(array, base):
    for i in range(len(array)):
        value = array[i][0] * base + array[i][1]
        array[i] = value
    return array


def sort_n_2(array):
    n = len(array)
    convert_to_n(array, n)
    array = counting_sort_idx(array, n, 1)
    array = counting_sort_idx(array, n, 0)
    convert_back(array, n)
    return array


# sort array of n numbers where max ceiling(log2(n)) are different
# create array of size log2(n) storing tuples - (value, number of repeats), sorted by value
# for each element from array[n] search binary in array of tuples and either add to number of repeats or add new element
def binary_search(array, key, max_index):
    p, r = 0, max_index
    while p < r:
        middle = (p + r) // 2
        if array[middle][0] == key:
            return middle
        elif array[middle][0] > key:
            r = middle
        else:
            p = middle + 1
    return -1


def add_new(array, free, key):
    # free - first index in array that still holds (-1, -1)
    p = free
    while p > 0 and array[p - 1][0] > key:
        array[p] = array[p - 1]
        p -= 1
    array[p] = [key, 1]


def sort(array):
    log2n = ceil(log2(len(array)))
    # add values to table holding how many times they are repeated
    max_index = 0
    diff_values = [[-1, -1]] * log2n
    for value in array:
        index = binary_search(diff_values, value, max_index)
        if index != -1:
            diff_values[index][1] += 1
        else:
            add_new(diff_values, max_index, value)
            max_index += 1
    # use diff_values to rewrite array
    current_index = 0
    for value, repeats in diff_values:
        if repeats == -1:
            break
        for i in range(repeats):
            array[current_index] = value
            current_index += 1


n = 10
test = [randint(1, ceil(log2(n))) for _ in range(n)]
print(test)
sort(test)
print(test)
