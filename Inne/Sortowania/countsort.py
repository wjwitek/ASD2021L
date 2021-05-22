def counting_sort(array, k):
    counts = [0] * (k + 1)
    sorted_array = [0] * len(array)
    for i in array:
        counts[i] += 1
    for i in range(1, k + 1):
        counts[i] = counts[i] + counts[i - 1]
    for i in range(k + 1):
        counts[i] -= 1
    for i in range(len(array) - 1, -1, -1):
        sorted_array[counts[array[i]]] = array[i]
        counts[array[i]] -= 1
    return sorted_array


def counting_sort_idx(array, k, index):
    counts = [0] * (k + 1)
    sorted_array = [0] * len(array)
    for i in array:
        counts[i[index]] += 1
    for i in range(1, k + 1):
        counts[i] = counts[i] + counts[i - 1]
    for i in range(k + 1):
        counts[i] -= 1
    for i in range(len(array) - 1, -1, -1):
        sorted_array[counts[array[i][index]]] = array[i]
        counts[array[i][index]] -= 1
    return sorted_array


test = [0, 2 , 5, 0, 4, 4]
print(counting_sort(test, 6))

