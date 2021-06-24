"""
Dla każdej litery alfabetu łacińskiego tworzymy listę indeksów z tą literą w słowie x i listę indeksów z tą literą w y.
Sprawdzamy czy są tej samej długości, a następnie obie lsty sortujemy. Jeśli wszystkie indeksy na odpowiadającyh sobie
miejscach w listach różnią się o co najwyżej t, to można utworzyć t-anagram.
Złożoność czasowa: O(nlogn)
Złożoność pamięciowa: O(n)
- countosrt zamiast sort i byłoby n :/
"""
from zad1testy import runtests


def compare(list_1, list_2, t):
    if len(list_1) != len(list_2):
        return False
    list_1.sort()
    list_2.sort()
    for i in range(len(list_2)):
        if abs(list_2[i] - list_1[i]) > t:
            return False
    return True


def tanagram(x, y, t):
    alphabet = [[[], []] for _ in range(26)]
    if len(x) != len(y):
        return False
    n = len(x)
    for i in range(n):
        alphabet[ord(x[i]) - ord('a')][0].append(i)
        alphabet[ord(y[i]) - ord('a')][1].append(i)
    for list_1, list_2 in alphabet:
        if not compare(list_1, list_2, t):
            return False
    return True


runtests(tanagram)