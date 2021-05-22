"""
Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogąbyć zarówno dodatnie jak
i ujemne):
n1+n2+...+nk
Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej kolejności, by największy co
do wartości bezwzględnej wynik tymczasowy (wynik każdej operacjidodawania; wartość końcowej sumy również traktujemy jak
wynik tymczasowy) był możliwie jak najmniejszy.  Aby  ułatwić  sobie  zadanie,  asystent  nie  zmienia  kolejności
liczb  w  sumie  a  jedynie wybiera kolejność dodawań. Napisz funkcję optsum, która przyjmuje tablicę liczb
n1, n2, . . . , nk(w kolejności w jakiej wystę-pują w sumie; zakładamy, że tablica zwiera co najmniej dwie liczby) i
zwraca największą wartość bezwzględną  wyniku  tymczasowego  w  optymalnej  kolejności  dodawań.  Na  przykład  dla
tablicy wejściowej: [1,−5,2] funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do
wyniku. Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową. Nagłówek funkcji optsum
powinien mieć postać:
def opt_sum(tab):
...

Jako koszt doania liczb od i do j włącznie rozumiem największy co do wartości bezwzględnej wynik tymczasowy. Wtedy:
f(i, j) - najmniejszy możliwy koszt dodani liczb od i do j włącznie
s(i, j) - suma liczb od i do j włącznie
f(i, j) = min{max{f(i+1, j), |s(i+1,j) + tab[i]|}, max{f(i, j-1), |s(i,j-1) + tab[j]|}}
s(i, j) = s(i, j-1) + tab[j]
f(i,i) = 0
s(i,i) = tab[i]
Przechowuję dwie tablice k x k, jedna zawierająca wyniki funkcji f(i, j), a druga wyniki funkcji s(i, j). Odpowiedzią
jest f(0, k-1).
Złożoność obliczniowa: O(n^2) - wypełnienie obu tablic metodą bottom-up.
"""


def opt_sum(tab):
    n = len(tab)
    f = [[-1 for _ in range(n)] for _ in range(n)]
    s = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        f[i][i] = 0
        s[i][i] = tab[i]
    for i in range(n):
        for j in range(i + 1, n):
            s[i][j] = s[i][j - 1] + tab[j]
    for k in range(1, n):
        i = 0
        j = i + k
        while i < n and j < n:
            f[i][j] = min(max(f[i+1][j], abs(s[i + 1][j] + tab[i])), max(f[i][j - 1], abs(s[i][j - 1] + tab[j])))
            i += 1
            j += 1
    return f[0][n - 1]


test = [1, -5, 2]
print(opt_sum(test))
