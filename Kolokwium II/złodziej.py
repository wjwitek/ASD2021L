"""
Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n−1]. Złodziej chce wybrać
przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu ukraść dwa przedmioty leżące obok siebie.
Proszę zaimplementować funkcję: int goodThief( int A[], int n ); która zwraca maksymalną wartość przedmiotów, które
złodziej może ukraść zgodnie ze swoim kodeksem moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę
uzasadnić poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie jak najszybszy
(ale przede wszystkim poprawny).
Algorytm opiera się na funkcji f(i) - maksymalna wartość przedmiotów ukradzioncych z pośród przedmiotów od 0 do i, gdzie
f(0) = A[0], f(1) = max(A[1], A[0]), f(i) = max(f(i - 1), f(i - 2) + A[i]), odpowiedzią jest f(n), wartościi f(i)
wyliczamy konstruując tablicę jednowymiarową długości n, na jej podstawie też odczytujemy numery kradzionych
przedmiotów.
"""


def good_thief(values):
    n = len(values)
    array = [-1 for _ in range(n)]
    array[0] = values[0]
    array[1] = max(values[0], values[1])
    for i in range(2, n):
        array[i] = max(array[i - 1], array[i - 2] + values[i])
    i = n - 1
    print("max value: ", array[n - 1])
    while i > 0:
        if i > 2 and values[i] == array[i] - array[i - 3]:
            print(i, end=" ")
            array[i] = -1
            i -= 3
        if i > 1 and values[i] == array[i] - array[i - 2]:
            print(i, end=" ")
            array[i] = -1
            i -= 2
        elif values[i] == array[i] - array[i - 1]:
            print(i, end=" ")
            array[i] = -1
            i -= 1
        else:
            i -= 1
    if array[2] == -1:
        print(0)
    else:
        if values[0] > values[1]:
            print(0)
        else:
            print(1)


test = [6, 5, 1, 2, 3, 6, 1]
good_thief(test)
