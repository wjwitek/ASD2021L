"""
Modification of Dijkstra each node can be visited twice - once for prev edge was added to cost and once for prev edge
was not added to cost. It also means two arrays of parent.
Time complexity: O(ElogV)
"""
from queue import PriorityQueue


def alicja_und_bob(G, a, b):
    n = len(G)
    shortest_true = [float('inf') for _ in range(n)]
    shortest_false = [float('inf') for _ in range(n)]
    parent_true = [None for _ in range(n)]
    parent_false = [None for _ in range(n)]
    # add starting point
    shortest_true[a] = shortest_false[a] = 0
    queue = PriorityQueue()
    queue.put((shortest_true[a], a, True))
    queue.put((shortest_false[a], a, False))
    while not queue.empty():
        length, node, flag = queue.get()
        if (flag and shortest_true[node] < length) or (not flag and shortest_false[node] < length):
            continue
        if flag:
            for i in range(n):
                if G[node][i] != 0 and shortest_false[i] > length:
                    shortest_false[i] = length
                    parent_false[i] = node
                    queue.put((length, i, False))
        else:
            for i in range(n):
                if G[node][i] != 0 and shortest_true[i] > length + G[node][i]:
                    shortest_true[i] = length + G[node][i]
                    parent_true[i] = node
                    queue.put((shortest_true[i], i, True))
    if shortest_true[b] == shortest_false[b] == float('inf'):
        return None, None, None
    result = []
    flag = False
    shortest = shortest_false[b]
    if shortest_true[b] < shortest_false[b]:
        shortest = shortest_true[b]
        flag = True
    while b is not None:
        result.append(b)
        if flag:
            b = parent_true[b]
        else:
            b = parent_false[b]
        flag = not flag
    driver = 'Bob'
    if flag:
        driver = 'Alicja'
    return driver, shortest, result[::-1]


if __name__ == "__main__":
    from zad2testy import runtests
    runtests(alicja_und_bob)