"""
Dzilę na silnie spójn składowe, tworzę nowy graf, żeby znaleźć kolejność rytuałów i punkty startowe, szukam ścieżki.
"""


def dfs_matrix(matrix):
    n = len(matrix)
    visited = [False for _ in range(n)]
    time = [-1 for _ in range(n)]
    timer = 0

    def visit(vertex):
        nonlocal timer
        visited[vertex] = True
        for i in range(n):
            if matrix[vertex][i] != 0 and not visited[i]:
                visit(i)
        time[vertex] = timer
        timer += 1

    for j in range(n):
        if not visited[j]:
            visit(j)

    return time


# find strongly connected components for graph represented as adjacency matrix
def sss(graph):
    times = dfs_matrix(graph)
    n = len(graph)
    # reverse graph
    reversed_graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                reversed_graph[j][i] = graph[i][j]

    result = []
    visited = [False for _ in range(n)]
    times = [[times[x], x] for x in range(n)]
    times.sort(reverse=True)

    def visit(vertex, sign):
        visited[vertex] = True
        result[sign].append(vertex)
        for i in range(n):
            if reversed_graph[vertex][i] != 0 and not visited[i]:
                visit(i, sign)

    sign = 0
    for _, i in times:
        if not visited[i]:
            result.append([])
            visit(i, sign)
            sign += 1
    return result


def nadgorliwy_mag(G) -> list:
    components = sss(G)
    for row in components:
        print(row)


G_1 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

G_2 = [[0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0]]

G_3 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]






# niżej proszę nie patrzeć :))




odp_1 = [[0, 2, 1, 3], [7, 8, 10, 9], [4, 6, 5]]
odp_2 = [[0], [1, 2, 3, 4, 6, 7], [5, 8]]
odp_3 = [[0, 2, 1], [6, 8, 7], [4, 3, 5], [9, 11, 10]]






































































































def valid_cycle(G, cycle_1, cycle_2):
    if len(cycle_1) != len(cycle_2):
        return False
    for el in cycle_2:
        if el not in cycle_1:
            return False
    return True


def check_solution(solution, correct):
    if len(solution) != len(correct):
        return False



if __name__ == "__main__":
    test = [(G_1, odp_1), (G_2, odp_2), (G_3, odp_3)]
    problem = False
    for i in range(len(test)):
        result = check_solution(test[i][0], nadgorliwy_mag(test[i][0]), test[i][1])
        if result == 2:
            print("Test", i + 1, ": nieprawidłowa odpowiedź.")
            problem = True
        elif result == 3:
            print("Test", i + 1, ": prawdopodobnie błędne przypisanie wież do jednego rytuału.")
            problem = True
        elif result == 4:
            print("Test", i + 1, ": próba przejścia pomiędzy wieżami nieistniejącym teleportem.")
            problem = True
        elif result == 5:
            print("Test", i + 1, ": niewłaściwa liczba rytuałów.")
            problem = True
        else:
            print("Test", i + 1, "ok.")
    if not problem:
        print("Wszystko ok <3")
