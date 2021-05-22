from quicksort import partition


# mandatory problems - my implementation - quicksort tail call optimisation
def less_memory_quicksort(tab, left, right):
    while left < right:
        q = partition(tab, left, right)
        if q - left < right - q:
            less_memory_quicksort(tab, left, q - 1)
            left = q + 1
        else:
            less_memory_quicksort(tab, q + 1, right)
            right = q - 1


# mandatory problems - my implementation - insert new element to heap (maximum heap assumed)
def sort_out_key(heap, i):
    # this function gets index of newly added element and moves it into correct position
    parent = (i - 1) // 2
    while i > 0 and heap[i] > heap[parent]:
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
        parent = (i - 1) // 2


def heap_insert(heap, new_element):
    # if append cant be used i would just copy elements to new array
    heap.append(new_element)
    sort_out_key(heap, len(heap) - 1)
