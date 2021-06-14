"""
Kapitan pewnego statku zastanawia sie, czy moze wpłynac do portu mimo tego, ze nastapił
odpływ. Do dyspozycji ma mape zatoki w postaci tablicy:
int n = ...
int m = ...
int A[m][n];
gdzie wartosc A[y][x] to głebokosc zatoki na pozycji (x, y). Jesli jest ona wieksza niz pewna
wartosc int T to statek moze sie tam znalezc. Poczatkowo statek jest na pozycji (0, 0) a port
znajduje sie na pozycji (n − 1,m − 1). Z danej pozycji statek moze przepłynac bezposrednio
jedynie na pozycje bezposrednio obok (to znaczy, na pozycje, której dokładnie jedna ze
współrzednych rózni sie o jeden). Prosze napisac funkcje rozwiazujaca problem kapitana.
Pomysł: BFS z warunkiem przejścia na inną pozycję, sprawdzamy czy port jest visited.
Złożoność czasowa: O(m*n)
"""
from collections import deque


def find_moves(array, m, n, T, visited, x, y):
    moves = []
    if x - 1 >= 0 and array[x - 1][y] > T and not visited[x - 1][y]:
        moves.append((x - 1, y))
    if x + 1 < m and array[x + 1][y] > T and not visited[x + 1][y]:
        moves.append((x + 1, y))
    if y + 1 < n and array[x][y + 1] > T and not visited[x][y + 1]:
        moves.append((x, y + 1))
    if y - 1 >= 0 and array[x][y - 1] > T and not visited[x][y - 1]:
        moves.append((x, y - 1))
    return moves


def captain(array, m, n, T):
    queue = deque()
    counter = 1
    queue.append((0, 0))
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    while counter > 0:
        x, y = queue.popleft()
        counter -= 1
        moves = find_moves(array, m, n, T, visited, x, y)
        for new_x, new_y in moves:
            visited[new_x][new_y] = True
            queue.append((new_x, new_y))
            counter += 1
    return visited[m - 1][n - 1]
