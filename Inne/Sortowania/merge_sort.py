from random import randint


#  merge sort using as little memory as possible
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


def merge_sort(array_to_sort):
    temp = [0] * len(array_to_sort)

    def merge_sort_recursion(array, p, r):
        if p < r:
            middle = (p + r) // 2
            merge_sort_recursion(array, p, middle)
            merge_sort_recursion(array, middle + 1, r)
            merge(array, p, middle, middle + 1, r, temp)

    merge_sort_recursion(array_to_sort, 0, len(array_to_sort) - 1)


test = [randint(1, 100) for _ in range(10)]
print(test)
merge_sort(test)
print(test)
