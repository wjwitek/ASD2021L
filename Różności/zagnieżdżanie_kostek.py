"""
Sprawdzanie zagnieżdżania:
1. Sortujemy malejąco wierzchołki w obu kostkach.
2. Sprawdzamy, czy dla każdego i xi < yi.
Właściwy algorytm:
1. Tworzymy DAG gdzie krawędzie są od większej kostki do zawieranej kostki.
2. Sortowanie topologiczne.
3. Dynamiczne: f(i) = max po (j,i) {f(j) + 1}
wierzchołki których parent po sortowaniu jest None.
Złożoność czasowa: O(n*dlogd+n^2d+n^2logn)
"""
from queue import PriorityQueue


# check if dice first can be in dice second
def compare_dice(first, second):
    # sorting is done in main function
    for i in range(len(first)):
        if first[i] >= second[i]:
            return False
    return True


def longest_sequence(dices):
    n = len(dices)
    # creating DAG
    for i in range(n):
        dices[i].sort(reverse=True)
    graph = [[] for _ in range(n)]
    reversed_graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if compare_dice(dices[j], dices[i]):
                graph[i].append([j])
                reversed_graph[j].append(i)
    # topological sort
    visited = [False for _ in range(n)]
    result = []

    def DFSVisit(v):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                DFSVisit(u)
        result.append(v)

    for i in range(n):
        if not visited[i]:
            DFSVisit(i)

    # calculate values of f(i)
    result = result[::-1]
    distance = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    for i in result:
        biggest = 0
        for j in reversed_graph[i]:
            if distance[j] + 1 > biggest:
                biggest = distance[j] + 1
                parent[i] = j
        distance[i] = biggest

    # create longest path
    biggest = 0
    for i in range(1, n):
        if distance[biggest] < distance[i]:
            biggest = i
    path = [biggest]
    while parent[biggest] is not None:
        path.append(parent[biggest])
        biggest = parent[biggest]
    return path[::-1]
