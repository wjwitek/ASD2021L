# Weronika Witek
from zad1testy import runtests
"""
Algorytm polega na wybraniu za pomocą quickselect najpierw elementu (n**2 - n)//2 + 1 co do kolejności (rosnącej), a następnie n - 1 pierwszego spośród elementów
po prawej stronie pierwszego wybranego elementu. Dzięki użyciu quickselect przed pierwszym elementem w tablicy są same liczby mniejsze od niego (te które
należy wpisać pod przekątną, pomiędzy wybranymi elementami włącznie znajdują się liczby, które należy wpisać nad przekątną, a za drugim elementem te, które
trzeba wpisać nad przekątną.
Algorytm ma złożność czasową O(n^2), bo taką złożoność mają zarówno quickselect (dla n^2 elementów) jak i przepisanie elementów.
Algorytm ma złożoność pamięciową O(n^2) - tyle ile zajmuje tablica danych wejściowych
"""


# standardowy quickselect, tylko na tablicy 2D (zlinearyzowanej)
def partition(tab, p, r, n):
    # p, r - przedział w którym działa partition (obustronnie domknięty)
    # n - długość tablicy (do linearyzacji)
    x = tab[r // n][r % n]
    i = p - 1
    for j in range(p, r):
        if tab[j // n][j % n] <= x:
            i += 1
            tab[i // n][i % n], tab[j // n][j % n] = tab[j // n][j % n], tab[i // n][i % n]
    tab[(i + 1) // n][(i + 1) % n], tab[r // n][r % n] = tab[r // n][r % n], tab[(i + 1) // n][(i + 1) % n]
    return i + 1


def quick_select(tab, start, end, i, n):
    if start >= end:
        return tab[start // n][start % n]
    q = partition(tab, start, end, n)
    k = q - start + 1
    if k == i:
        return tab[q // n][q % n]
    elif i < k:
        return quick_select(tab, start, q - 1, i, n)
    else:
        return quick_select(tab, q + 1, end, i - k, n)


def rewrite(tab, p, r, n):
    # p i r to indeksy oznaczające (domknięty) przedział liczb na przekątną
    # najpierw ustawiwamy przekątną
    free_above = (n + 1) // 2
    free_below = 0
    for i in range(p, r + 1):
        if i // n == i % n:
            continue # liczba już jest na przekątnej (dla n nieparzystych jedna taka będzie)
        elif i // n < i % n:
            # liczba którą trzeba przenieść na przekątna jest nad przekątną - trzeba zamienić z częścią przekątnej zawierającą elementy większe
            tab[free_above][free_above], tab[i // n][i % n] = tab[i // n][i % n], tab[free_above][free_above]
            free_above += 1
        else:
            # liczba którą trzeba przenieść na przekątna jest pod przekątną - trzeba zamienić z częścią przekątnej zawierającą elementy mniejsze
            tab[free_below][free_below], tab[i // n][i % n] = tab[i // n][i % n], tab[free_below][free_below]
            free_below += 1
    # po tych operacji elementy z przekątnej i w zakresie indeksów [p,r] są na swoich miejscach
    # pozostaje zamiana elementów nad przekątną z tymi pod przekątna
    for row in range(0, p // n):
        for col in range(row + 1, n):
            tab[row][col], tab[n - 1 - row][n - 1 - col] = tab[n - 1 - row][n - 1 - col], tab[row][col]


def Median(T):
    n = len(T)
    quick_select(T, 0, n ** 2 - 1, (n**2 - n) // 2 + 1, n)
    quick_select(T, (n**2 - n) // 2 + 2, n ** 2 - 1, n - 1, n)
    print(T)
    rewrite(T, (n**2 - n) // 2, (n**2 - n) // 2 + n - 1, n)
    return

runtests( Median ) 
