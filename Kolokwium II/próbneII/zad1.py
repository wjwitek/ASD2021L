"""
Używając dwóch kolejek przechodzę od liści w górę do momentu aż w kolejce nie mam dokładnie tylu elementów ile jeszcze
jest niesprawdzonych, tj. counter = 0 - dowolny z nich może być korzeniem.
"""


from zad1testy import runtests
from queue import Queue


def best_root(L):
    n = len(L)
    visited = [False for _ in range(n)]
    queue_1 = []
    queue_2 = []
    counter = n
    switch = True
    for i in range(n):
        if len(L[i]) == 1:
            queue_2.append(i)
            counter -= 1
            visited[i] = True
    while counter > 0:
        if switch:
            while not len(queue_2) == 0:
                u = queue_2.pop()
                for i in L[u]:
                    if not visited[i]:
                        visited[i] = True
                        queue_1.append(i)
                        counter -= 1
            switch = not switch
        else:
            while not len(queue_1) == 0:
                u = queue_1.pop()
                for i in L[u]:
                    if not visited[i]:
                        visited[i] = True
                        queue_2.append(i)
                        counter -= 1
            switch = not switch

    if switch:
        return queue_2.pop()
    return queue_1.pop()


runtests( best_root )