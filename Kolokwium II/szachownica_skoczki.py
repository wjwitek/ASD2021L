"""
Szachownica NxN, ustawiono pewną ilość skoczków. Opisać algorytm który sprawdzi czy jest możliwa sekwencja ruchów
spełniająca:
- każdy ruch kończy się zbiciem skoczka
- sekwencja kończy się gdy zostanie jeden skoczek.
Reprezentuje problem jako graf, którego wierzchołami są skoczki, a krawędzie występują pomiędzy skoczkami, które mogą
się zbić (zakładam, że skoczki nie mogą przechodzić nad sobą bez zbicia, tj, jeśli są w lini ukośnej skoczki a, b, c, to
a nie może zbić c i vice versa. Następnie wyznaczam kolejność usuwania wierzchołków, która nie powoduje rozspójnienia
grafu  - DFSvisited zaczynając z losowego wierczhołka + oznacznie przetworzonych wierzchołków jako processed
(analogicznie do sprawdzania czy można usunąć wierzchołki w takiej kolejności, aby graf cały czas był spójny, z tym, że
tu zamiast usuwać wierzchołi, to zwijamy krawędzie). Jeśli po zakończeniu DFS wszystkie wierzchołki są processed, to
istnieje taka sekwencja ruchów.
Złożoność obliczeniowa: O(n^2)
"""


from queue import LifoQueue


def check_moves(i, j, num, graph, board):
    n = len(board)
    if i > 1 and j > 0 and board[i - 2][j - 1] != -1:
        graph[num].append(board[i - 2][j - 1])
    if i > 0 and i > 1 and board[i - 1][j - 2] != -1:
        graph[num].append(board[i - 1][j - 2])
    if i < n - 1 and j > 1 and board[i + 1][j - 2] != -1:
        graph[num].append(board[i + 1][j - 2])
    if i < n - 2 and j > 0 and board[i + 2][j - 1] != -1:
        graph[num].append(board[i + 2][j - 1])
    if i > 1 and j < n - 1 and board[i - 2][j + 1] != -1:
        graph[num].append(board[i - 2][j + 1])
    if i > 0 and j < n - 2 and board[i - 1][j + 2] != -1:
        graph[num].append(board[i - 1][j + 2])
    if i < n - 1 and j < n - 2 and board[i + 1][j + 2] != -1:
        graph[num].append(board[i + 1][j + 2])
    if i < n - 2 and j < n - 1 and board[i + 2][j + 1] != -1:
        graph[num].append(board[i + 2][j + 1])


# assumes positions of knight are given as 1 in matrix 2D
def chess(board):
    n = len(board)
    # count knights and assign them numbers
    counter = 0
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                board[i][j] = counter
                counter += 1
            else:
                board[i][j] = -1
    # create graph
    graph = [[] for _ in range(counter)]
    for i in range(n):
        for j in range(n):
            if board[i][j] != -1:
                check_moves(i, j, board[i][j], graph, board)
    # DFS visited
    visited = [False for _ in range(counter)]
    processed = [False for _ in range(counter)]
    indexes = [0 for _ in range(counter)]
    queue = LifoQueue()
    queue.put(0)
    visited[0] = True
    while not LifoQueue.empty():
        temp = LifoQueue.get()
        while indexes[temp] < len(graph[temp]) and visited[graph[temp][indexes[temp]]]:
            indexes[temp] += 1
        if indexes[temp] < len(graph[temp]):
            visited[graph[temp][indexes[temp]]] = True
            queue.put(temp)
            queue.put(graph[temp][indexes[temp]])
            indexes[temp] += 1
        else:
            processed[temp] = True
    for i in range(counter):
        if not processed[i]:
            return False
    return True

