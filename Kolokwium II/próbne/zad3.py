"""
Sortujemy tablicę, a następnie metodą bottom-up budujemy tablicę najmniejszych kosztów dotarcia na kolejne liczby.
f(i) - najmniejszy możliwy koszt dojścia na liczbę pod indeksem i
Złożoność czasowa: O(n^2)
"""


from zad3testy import runtests
from queue import Queue


def find_cost(P):
    P = sorted(P)
    n = len(P)
    queue = Queue()
    # check which digits each number has
    digits = [[False for _ in range(10)] for _ in range(n)]
    costs = [float('inf') for _ in range(n)]
    costs[0] = 0
    for i in range(n):
        temp = P[i]
        while temp > 0:
            digits[i][temp % 10] = True
            temp //= 10
    # for each number determine where it can go and what cost would it be
    """
    for i in range(n - 1):
        for j in range(n):
            # should be from 0 not i + 1
            for k in range(10):
                if digits[i][k] and digits[j][k] and costs[j] > costs[i] + abs(P[i] - P[j]):
                    costs[j] = costs[i] + abs(P[i] - P[j])
                    break
    """
    for j in range(1, n):
        for k in range(10):
            if digits[0][k] and digits[j][k] and costs[j] > costs[0] + abs(P[0] - P[j]):
                costs[j] = costs[0] + abs(P[0] - P[j])
                queue.put(j)
                break
    while not queue.empty():
        i = queue.get()
        for j in range(n):
            if j == i:
                continue
            for k in range(10):
                if digits[i][k] and digits[j][k] and costs[j] > costs[i] + abs(P[i] - P[j]):
                    costs[j] = costs[i] + abs(P[i] - P[j])
                    queue.put(j)
                    break
    if costs[n - 1] == float('inf'):
        return -1
    else:
        return costs[n - 1]


runtests(find_cost)
test = [129, 758, 759, 888]
print(find_cost(test))
