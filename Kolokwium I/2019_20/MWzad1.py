""" Algorytm zapisuje do pomocniczej tablicy liczbę cyfr jednokrotnych, wielokrotnych oraz obecny indeks danego elementu, następnie sortuje je
 przez sortowania pozycyjnie i na podstawie obecnego położenia w tablicy pomocniczej przepisuje tablicę wejściową"""


def change(B, n, i):
    A = [0] * 10
    while n > 0:
        A[n % 10] += 1
        if A[n % 10] == 1:
            B[i][0] += 1
        elif A[n % 10] == 2:
            B[i][0] -= 1
            B[i][1] += 1
        n //= 10


def countsort(A, j):
    n = len(A)
    C = [0] * 10
    B = [0] * n
    for x in A:
        C[x[j]] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        C[A[i][j]] -= 1
        B[C[A[i][j]]] = A[i]
    for i in range(n):
        A[i] = B[i]


def prettysort(T):
    n = len(T)
    B = [[0, 0, _] for _ in range(n)]     #tablica trzymająca cyfry pojedyncze, wielokrotne i indeks w tablicy T
    for i in range(n):
        change(B, T[i], i)               #wypełniam tablicę B poprzez funkcję change - jaką change ma złożoność nie wiem, chyba stała dla jednego elementu
    countsort(B, 1)                      #countersort po cyfrach wielokrotnych
    countsort(B, 0)                      #countersort po cyfrach jednokrotnych
    M = [0] * n
    for i in range(n):
        M[i] = T[B[n-i-1][2]]            #przepisanie do tablicy T
    for i in range(n):
        T[i] = M[i]
    print(T)

T = [123,455,114577,2344,67333]
prettysort(T)
