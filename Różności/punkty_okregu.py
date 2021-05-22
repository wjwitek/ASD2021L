"""
Mamy dane n punktów (x, y) w okręgu o promieniu k (liczba naturalna), tzn. 0 <= x2 + y2 <= k, które są w nim równomiernie rozłożone, tzn. prawdopodobieństwo znalezienia punktu na danym obszarze jest proporcjonalne do pola tego obszaru.
Napisz algorytm, który w czasie Θ(n) posortuje punkty po ich odległości do punktu (0, 0), tzn.
d = sqrt(x2 + y2).
"""


def insertion_sort_array(list_to_sort, index):
    n = len(list_to_sort)
    for i in range(n):
        el = list_to_sort[i]
        k = i - 1
        while el[index] < list_to_sort[k][index] and k > - 1:
            list_to_sort[k + 1] = list_to_sort[k]
            list_to_sort[k] = el
            k -= 1


def add_length(point, k):
    return point[0], point[1], ((point[0] ** 2 + point[1] ** 2) ** (1/2)) / k


def bucket_sort(array, k):
    n = len(array)
    for i in range(n):
        array[i] = add_length(array[i], k)
    buckets = [[] for _ in range(k + 1)]
    for value in array:
        buckets[int(k * value[2])].append(value)
    for i in range(k):
        if buckets[i]:
            insertion_sort_array(buckets[i], 2)
    index = 0
    for bucket in buckets:
        for element in bucket:
            array[index] = (element[0], element[1])
            index += 1


test = [(1, 0), (0, 1), (3, 0), (0, 2)]
bucket_sort(test, 3)
print(test)
