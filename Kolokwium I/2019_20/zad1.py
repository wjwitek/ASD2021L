"""
Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie jeden raz. Cyfra wielokrotna to taka,
która w liczbie występuje więcej niż jeden raz. Mówimy,że liczba naturalna A jest ładniejsza od liczby naturalnej
B jeżeli w liczbie A występuje więcej cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to
ładniejsza jest taliczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od 455,
liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.Dana jest tablica T zawierająca
liczby naturalne. Proszę zaimplementować funkcję:pretty_sort(T)która sortuje elementy tablicy T od najładniejszych
do najmniej ładnych. Użyty algorytmpowinien  być  możliwie  jak  najszybszy.  Proszę  w  rozwiązaniu  umieścić  1-2
zdaniowy  opisalgorytmu oraz proszę oszacować jego złożoność czasową
"""


def evaluate_number(num):
    # calculate number of single and repeated digits
    digits = [0] * 10
    while num > 0:
        digits[num % 10] += 1
        num //= 10
    single = repeated = 0
    for i in range(10):
        if digits[i] == 1:
            single += 1
        elif digits[i] > 1:
            repeated += 1
    return single, repeated


def convert_array(array):
    max_single = max_repeated = 0
    for i in range(len(array)):
        a, b = evaluate_number(array[i])
        array[i] = [array[i], a, b]
        if a > max_single:
            max_single = a
        if b > max_repeated:
            max_repeated = b
    return max_single, max_repeated


def convert_array_back(array):
    for i in range(len(array)):
        array[i] = array[i][0]
    return array


def count_sort_idx(array, k, index):
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


def count_sort_idx_reversed(array, k, index):
    n = len(array)
    counts = [0] * (k + 1)
    sorted_array = [0] * len(array)
    for i in array:
        counts[i[index]] += 1
    for i in range(1, k + 1):
        counts[i] = counts[i] + counts[i - 1]
    for i in range(k + 1):
        counts[i] -= 1
    for i in range(n - 1, -1, -1):
        sorted_array[n - 1 - counts[array[i][index]]] = array[i]
        counts[array[i][index]] -= 1
    return sorted_array


# variation of radix sort - first stable sort by repeated digits (min to max),
# than stable sort by single digits (max to min)
# time complexity - O(n)
def pretty_sort(array):
    max_single, max_repeated = convert_array(array)
    array = count_sort_idx(array, max_repeated, 2)
    array = count_sort_idx_reversed(array, max_single, 1)
    convert_array_back(array)
    return array


test = [122233, 34576, 24555777, 2233444, 789]
print(pretty_sort(test))
