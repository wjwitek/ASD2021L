""""
Dany jest zbiór przedziałów otwartych A={(a1, b1), ...,(an, bn)}. Proszę zaproponować algorytm (bez implementacji),
który znajduje taki zbiór X, X⊆{1, ..., n} że (a) |X|=k (gdzie k∈N to dany parametr wejściowy), (b) dla każdych i,j∈X,
przedziały (ai, bi) oraz (aj, bj) nie nachodzą na siebie, oraz (c) wartość maxj∈Xbj−mini∈Xai jest minimalna. Jeśli
podzbioru spełniającego warunki (a) i (b) nie ma, to algorytm powinien to stwierdzić. Algorytm powinien być możliwie jak
najszybszy (ale przede wszystkim poprawny).
Złożoność czasowa: O(n^2)
"""


def subset_of_sets(array, k):
    n = len(array)
    array.sort(key=lambda x: (x[1], x[0]))
    found = False
    result_1 = [-1 for _ in range(k)]
    result_2 = [-1 for _ in range(k)]
    minimum = float('inf')
    switch = True
    for i in range(n):
        mina = array[i][0]
        maxb = array[i][1]
        if switch:
            result_1[0] = i
        else:
            result_2[0] = i
        counter = 1
        j = i + 1
        while j < n - k:
            if array[j][0] > maxb:
                maxb = array[j][1]
                if switch:
                    result_1[counter] = j
                else:
                    result_2[counter] = j
                counter += 1
                if counter == k and maxb - mina < minimum:
                    minimum = maxb - mina
                    switch = not switch
                    found = True
            j += 1
    if not found:
        return None
    elif switch:
        return result_2
    else:
        return result_1
