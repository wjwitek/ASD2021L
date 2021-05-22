# Weronika Witek
"""
Funkcja create_information tworzy dla każdego elemntu tablicy k nową tablicę zawierająca indeksy elementów
występująych po k, takich, że są większe niż element k i mogą z elementem k utworzyć maksymalny podciąg (tj, maksymnalny
podciąg rosnący zawierjacy element k znajdyjący się w częsci tablicy od indeksu do n), a także dla
każdego elemntu przechowuje długość tego maksymalnego podciągu i ostatni indeks na którym znajdują się w nowej tablicy
elementy tworzące podciągi z k.
Następnie funkcja print_rec rekurencyjnie wypisuje wszystkie możliwe przejścia.
Złożoność obliczeniowa: O((n po k) * k) - maksymalna łączna długość wszystkich wypisywanych podiciągów dla długości
najdłuższego podciągu równej k
Złożoność pamięciowa: O(n^2) - tyle miejsca zamuje tablica info
"""


def create_information(array):
    n = len(array)
    info = [[[-1]*n, 1, 0] for _ in range(n)]
    longest = 1  # stores length of longest subsequence in whole array
    # parts of info: where we could we go next, length of max subsequence for element,
    # last index in array of where we could go next
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if array[i] < array[j] and info[j][1] + 1 >= info[i][1]:
                if info[j][1] + 1 > info[i][1]:
                    # if we found element that allows for longer subsequence than all elements before change max length
                    # and "discard" previously stored indexes (by changing value of variable storing last index)
                    info[i][1] = info[j][1] + 1
                    info[i][2] = 0
                info[i][0][info[i][2]] = j  # add index of new element that can come in subsequence after array[i]
                info[i][2] += 1
                if info[i][1] > longest:
                    longest = info[i][1]
    return info, longest


count = 0


def print_rec(array, info, index, counter, storage):
    global count
    storage[counter] = array[index]
    if info[index][2] != 0:  # if we are not at the end of subsequence for each possible next move call print_rec after
        # adding new element to storage
        for i in range(info[index][2]):
            new_index = info[index][0][i]
            print_rec(array, info, new_index, counter + 1, storage)
    else:  # if we are at the end of subsequence print it
        for el in storage:
            print(el, end=" ")
        print()
        count += 1


def printAllLis(A):
    global count
    info, longest = create_information(A)
    for k in range(len(A)):  # start recursion for  all points where maximum length subsequence can be started
        if info[k][1] == longest:
            print_rec(A, info, k, 0, [-1] * longest)
    print(count)
