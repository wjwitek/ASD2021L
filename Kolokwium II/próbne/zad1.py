"""
Mamy nieskierowany graf G=(V,E) reprezentowany przez listę sąsiadów. Proszę zaimplementować funkcję, która otrzyma na w
ejściu graf G i zwróci długość najdłuższej “łatwej” ścieżki , gdzie łatwa ścieżka to taka, wktórej każdy stopień <= 2.
Proszę skrótowo wyjaśnić ideę algorytmu i oszacować złożoność obliczeniową i pamięciową.
Z każdego wierzchołka o stopniu == 1 lub równym 2 i mającym jednego sąsiada o stopniu większym niż 2,
uruchamiam pseudo-BFS (bo tak długo jak chcę zachować warunki zadania mogę przejść z wierchołka u tylko do jednego
wierzchołka v), zapisując dla każdego wierzchołka nadjdłuższą znalezioną ścieżkę.  Nie pominę w ten sposób ścieżek,
bo przez każdy wierchołek stopnia 2 można przejśc tylko na jeden sposób.
Złożoność obliczeniowa: O(V) - każdy wierzchołek odwiedzam najwyżej raz + odwiedzam tylko wierzchołki, które mają
conajwyżej dwóch sąsiadów (a więc odpada koszt przeglądania wszystkich krawędzi)
Złożoność pamięciowa: O(V) - tablica visited
"""


def find_length_of_path(T, start, visited):
    length = 0
    prev = start
    r = -1
    for i in T[start]:
        if len(T[i]) <= 2:
            length += 1
            r = i
    if r < 0:
        return 0
    visited[start] = True
    visited[r] = True
    while r != start:
        found = False
        for i in T[r]:
            if len(T[i]) <= 2 and i != prev:
                found = True
                prev = r
                r = i
                visited[r] = True
                length += 1
        if not found:
            return length
    return length


def easy_path(T):
    n = len(T)
    maximum = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            if len(T[i]) == 1:
                temp = find_length_of_path(T, i, visited)
                if temp > maximum:
                    maximum = temp
            elif len(T[i]) == 2 and (len(T[T[i][0]]) > 2 or len(T[T[i][1]]) > 2):
                temp = find_length_of_path(T, i, visited)
                if temp > maximum:
                    maximum = temp
    # trzeba osobno rozważyć przydak gdy są same cykle
    return maximum


T1 = [[1], [2, 0, 8, 4], [3, 1], [2], [1], [6], [7, 5], [6, 8], [1, 7]]
print("Git" if easy_path(T1) == 3 else "chuj nie dziala") # 3


T2 = [[1], [2, 0, 9, 12, 13], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6, 12, 13], [9, 7], [10, 8, 1, 12], [11, 9], [10], [7, 9, 1], [1, 7]]
print("Git" if easy_path(T2) == 4 else "chuj nie dziala") # 4
