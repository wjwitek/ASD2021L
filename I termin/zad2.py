"""
Weronika Witek
Wykorzystuje zmodyfikowany algorytm Dijsktry, traktując pola jako wierzchołk, w ten sposób, że dla każdego wierzchołka
zamiast jednego mam 4 pola visited/quickest, po jednym na każdąe skierowanie na wejściu do wierzchołka.
Do tego do kolejki dorzucamy czas jaki zajęło samo przejście z pola na pole.
Ponieważ każdy wierzchołek ma co najwyżej 4 krawędzie incydentne (E ~ V), to używam wersji Dijkstry z
kolejką priorytetową. Wierzchołki numeruje tak, jakbym linearyzowała tablicę, to jest pole o nr. wiersza i oraz nr.
kolumny j, to wierzchołek i * m + j.
Złożoność czasowa: O(n * m * log(n * m))
Złożoność pamięciowa: O(n * m), gdzie n to liczba wierszy a m to liczba kolumn
"""
from zad2testy import runtests
from queue import PriorityQueue


def time_calc(turn, next_turn):
    if turn == next_turn:
        return 0
    if turn == 0:
        if next_turn == 1 or next_turn == 3:
            return 1
        else:
            return 2
    if turn == 1:
        if next_turn == 2 or next_turn == 0:
            return 1
        else:
            return 2
    if turn == 2:
        if next_turn == 1 or next_turn == 3:
            return 1
        else:
            return 2
    if turn == 3:
        if next_turn == 2 or next_turn == 0:
            return 1
        else:
            return 2


# 0 - prawo, 1 - w dół, 2 - w lewo, 3 - w górę
def gen_moves(L, n, m, row, col, turn):
    # generate list of possible moves with times of turn
    result = []
    if row < n - 1 and L[row + 1][col] != 'X':
        result.append([row + 1, col, time_calc(turn, 1) * 45, 1])
    if row > 0 and L[row - 1][col] != 'X':
        result.append([row - 1, col, time_calc(turn, 3) * 45, 3])
    if col < m - 1 and L[row][col + 1] != 'X':
        result.append([row, col + 1, time_calc(turn, 0) * 45, 0])
    if col > 0 and L[row][col - 1] != 'X':
        result.append([row, col - 1, time_calc(turn, 2) * 45, 2])
    return result


def speed(current_speed):
    if current_speed == 60:
        return 40
    return 30


def robot(L, A, B):
    n = len(L)
    m = len(L[0])
    num = n * m
    quickest = [[float('inf') for _ in range(4)] for _ in range(num)]
    queue = PriorityQueue()
    start_col, start_row = A
    # ruchy z pola A rozważam poza kolejką, żeby nie było problemu jaką prędkość na wejściu do pola A przypisać
    moves = gen_moves(L, n, m, start_row, start_col, 0)
    for i in range(4):
        quickest[start_row * m + start_col][i] = 0
    for row, col, time, turn in moves:
        quickest[row * m + col][turn] = time + 60
        queue.put((time + 60, row * m + col, turn, 60))
    while not queue.empty():
        time_used, node, turn, s = queue.get()
        moves = gen_moves(L, n, m, node // m, node % m, turn)
        for row, col, time, next_turn in moves:
            if time == 0:
                how_fast = speed(s)
            else:
                how_fast = 60
            if quickest[row * m + col][next_turn] > time_used + time + how_fast:
                quickest[row * m + col][next_turn] = time_used + time + how_fast
                queue.put((time_used + time + how_fast, row * m + col, next_turn, how_fast))
    minimum = min(quickest[B[1] * m + B[0]])
    if minimum == float('inf'):
        minimum = None
    return minimum

    
runtests( robot )


