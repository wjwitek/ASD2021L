from simplesort import insertion_sort_array


def bucket_sort(array):
    bucket = [0] * len(array)
    for i in range(len(bucket)):
        bucket[i] = []
    for num in array:
        bucket[int((num * 100) // 10)].append(num)
    for i in range(len(bucket)):
        insertion_sort_array(bucket[i])
    idx = 0
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            array[idx] = bucket[i][j]
            idx += 1


test = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
bucket_sort(test)
print(test)