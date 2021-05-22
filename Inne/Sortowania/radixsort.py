def counting_sort(array, k, idx):
    counts = [0] * (k + 1)
    sorted_array = [0] * len(array)
    for i in array:
        counts[i[idx]] += 1
    for i in range(1, k + 1):
        counts[i] = counts[i] + counts[i - 1]
    for i in range(k + 1):
        counts[i] -= 1
    for i in range(len(array) - 1, -1, -1):
        sorted_array[counts[array[i][idx]]] = array[i]
        counts[array[i][idx]] -= 1
    return sorted_array


def radix_sort(array, d):
    for i in range(d, -1, -1):
        array = counting_sort(array, 9, i)
    return array
