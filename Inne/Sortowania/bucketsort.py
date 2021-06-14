from simplesort import insertion_sort_array


def bucket_sort(array, a, b, idx=None):
    # a, b is range of numbers in array (assuming normal distribution)
    n = len(array)
    bucket = [[] for _ in range(n)]
    if idx is not None:
        for num in array:
            if num[idx] == b:
                bucket[n - 1] = num
                continue
            bucket[int((num[idx] - a) * n)].append(num)
        for i in range(len(bucket)):
            insertion_sort_array(bucket[i], idx)
    else:
        for num in array:
            if num == b:
                bucket[n - 1] = num
                continue
            bucket[int((num - a) * n)].append(num)
        for i in range(len(bucket)):
            insertion_sort_array(bucket[i])
    idx = 0
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            array[idx] = bucket[i][j]
            idx += 1


test = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
bucket_sort(test, 0, 1)
print(test)