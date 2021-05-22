# check the heap (according to maximum property)
"""def max_heapify(tab, i, heap_size):
    largest = i
    # identify largest node
    if 2 * (i + 1) - 1 < heap_size and tab[2 * (i + 1) - 1] > tab[largest]:
        largest = 2 * (i + 1) - 1
    if 2 * (i + 1) < heap_size and tab[2 * (i + 1)] > tab[largest]:
        largest = 2 * (i + 1)
    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        max_heapify(tab, largest, heap_size)"""


# check the heap without using recursion
def max_heapify_iter(tab, i, heap_size):
    k = i
    while k < heap_size:
        largest = k
        if 2 * (k + 1) - 1 < heap_size and tab[2 * (k + 1) - 1] > tab[largest]:
            largest = 2 * (k + 1) - 1
        if 2 * (k + 1) < heap_size and tab[2 * (k + 1)] > tab[largest]:
            largest = 2 * (k + 1)
        if largest != k:
            tab[k], tab[largest] = tab[largest], tab[k]
            k = largest
        else:
            break


# build the heap based on a table of values
def build_max_heap(tab):
    for i in range(len(tab) // 2, -1, -1):
        max_heapify_iter(tab, i, len(tab))


# use heap to sort list
def heapsort(tab):
    build_max_heap(tab)
    heap_size = len(tab)
    for i in range(len(tab) - 1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heap_size -= 1
        max_heapify_iter(tab, 0, heap_size)
