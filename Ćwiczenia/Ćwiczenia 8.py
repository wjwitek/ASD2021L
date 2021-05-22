from queue import Queue


# Algorytm sprawdzający czy graf jest dwudzielny.
def check_graph(list_of_neighbours):
    # assumes that graph is in form of list of lists
    n = len(list_of_neighbours)
    vis_queue = Queue(n)
    side = [-1 for _ in range(n)]
    parents = [-1 for _ in range(n)]
    side[0] = 1
    vis_queue.put(0)
    while not vis_queue.empty():
        u = vis_queue.get()
        if side[parents[u]] == 1:
            side[u] = 2
        else:
            side[u] = 1
        for v in list_of_neighbours[u]:
            if side[v] == -1:
                parents[v] = u
                vis_queue.put(v)
            elif side[v] == side[u]:
                return False
    return True


test = [[3, 4, 5], [4, 2], [3, 4, 5], [0, 2], [0, 1, 2], [0, 2]]
print(check_graph(test))
