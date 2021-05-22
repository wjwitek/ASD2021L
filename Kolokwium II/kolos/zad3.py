"""
Weronika Witek
Założenie: jeśli dwa pola stykają się tylko wierzchołkiem, to nie tworzą razem jednej plamy ropy (np. (0, 0) i (1, 1))
Korzystając z algorytmu BFS, traktując pola w tablicy T jako wierzchołki, pomiędzy którymi istnieje krawedż, jeśli
sąsiadują ze sobą, obliczam sumaryczne objętości ropy dostępnej z pól w wierszu zerowym. Jeśli do danej plamy ropy jest
dostęp w kilku miejscach na trasie, to objętość tą zapisuje na pierwszym miejscu, a w pozostałych zero, bo nie mamy
ograniczenia na objętość baku, więc jeśli mielibyśmy brać daną objętość, to równie dobrze można ją wziąć wcześniej.
Następnie metodą bottom-up obliczam wartości funkcji f(i, k) = najmniejsza liczba przystanków potrzebna, żeby dotrzeć na
pole i mając conajmniej k litrów paliwa oraz parent(i) = plama ropy na której tankowaliśmy ostatnio w najlepszym
rozwiązaniu.
Złożoność czasowa: O(n^3)
Złożoność pamięciowa: O(n^2)
W ostatnim teście mój algorytm podaje inny wynik niż zakłada test, ale jest on również poprawny.
"""


from zad3testy import runtests
from queue import PriorityQueue


def plan(T):
    n = len(T)
    queue = PriorityQueue()
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    # obliczanie objętości plam
    for i in range(n):
        if T[0][i] != 0:
            priority = 0
            volume = T[0][i]
            T[0][i] = 0
            queue.put((priority, 0, i))
            priority += 1
            while not queue.empty():
                _, x_0, y_0 = queue.get()
                for x, y in moves:
                    if -1 < x_0 + x < n and -1 < y_0 + y < n and T[x_0 + x][y_0 + y] != 0:
                        volume += T[x_0 + x][y_0 + y]
                        T[x_0 + x][y_0 + y] = 0
                        queue.put((priority, x_0 + x, y_0 + y))
            T[0][i] = volume
    # obliczanie wartości funkcji f i parent
    f = [[-1 for _ in range(n)] for _ in range(n)]  # pojemność baku ograniczam do n, bo mając n litrów można dotrzeć od razu na koniec
    parent = [[None for _ in range(n)] for _ in range(n)]
    f[0][0] = 0
    for i in range(n):
        if T[0][i] != 0:
            j = 0
            while j < n and f[i][j] != -1:
                petrol = j + T[0][i]
                for l in range(i + 1, min(n, i + petrol + 1)):
                    remaining = min(petrol - (l - i), n - 1)
                    for k in range(remaining + 1):
                        if f[l][k] == -1 or f[i][j] + 1 < f[l][k]:
                            f[l][k] = f[i][j] + 1
                            parent[l][k] = i
                j += 1
    # odtwarzanie ścieżki
    least = -1
    for i in range(n):
        if f[n - 1][i] != -1 and (f[n - 1][least] == -1 or f[n - 1][least] > f[n - 1][i]):
            least = i
    if least == -1:
        return None
    index = n - 1
    result = []  # można oczywiście użyć tablicy długości n i indeksu, ale tak jest czytelniej
    index = parent[index][least]
    least = least + (n - 1 - index) - T[0][index]
    while parent[index][least] is not None:
        result.append(index)
        temp = index
        index = parent[index][least]
        least = least + (temp - index) - T[0][index]
    result.append(0)
    return result[::-1]


runtests(plan)
