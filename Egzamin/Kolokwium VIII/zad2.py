"""
Problem plecakowy, ale taki 3D, gdzie ograniczeniami są pieniądze i liczba kart.
F(i, j, k) - największy zysk jaki możńa osiognąc wybierając z kart do i włącznie nie przekraczając ceny j i liczby k
kart.
Założenie: żadna karta nie ma ceny > D (nie chce mi się tego oifować)
Złożoność czasowa: O(n * x * D)
"""


class NIEkarta:
    def __init__(self, cena, wartosc):
        self.cena = cena
        self.wartosc = wartosc


def starszy_pasjonat(T, x, D):
    n = len(T)
    arr = [[[0 for _ in range(x + 1)] for _ in range(D + 1)] for _ in range(n)]
    for i in range(T[0].cena, D + 1):
        for j in range(1, x + 1):
            arr[0][i][j] = T[0].wartosc
    for i in range(1, n):
        for j in range(1, D + 1):
            for k in range(1, x + 1):
                arr[i][j][k] = arr[i - 1][j][k]
                if j >= T[i].cena:
                    arr[i][j][k] = max(arr[i][j][k], arr[i - 1][j - T[i].cena][k - 1] + T[i].wartosc)
    result = []
    i, j, k = n - 1, D, x
    while True:
        if j < 0 or k < 0 or i < 0:
            break
        if j > 0 and arr[i][j][k] == arr[i][j - 1][k]:
            j -= 1
        elif k > 0 and arr[i][j][k - 1] == arr[i][j][k]:
            k -= 1
        elif i > 0 and arr[i][j][k] == arr[i - 1][j][k]:
            i -= 1
        else:
            result.append(i)
            i -= 1
    return result[::-1]


from copy import deepcopy
T = [NIEkarta(5,10), NIEkarta(5,5), NIEkarta(9,1), NIEkarta(10,2)]
cp = deepcopy(T)
x = 2
D = 10
print(starszy_pasjonat(T,x,D),[0, 1])

T = [NIEkarta(5,10), NIEkarta(2,5), NIEkarta(4,6), NIEkarta(1,2)]
x = 3
D = 9
print(starszy_pasjonat(T,x,D),[0,1,3])
