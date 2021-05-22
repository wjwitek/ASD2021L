from node_functions import Node
# in each function sorting from smallest to biggest


# insertion sort for array [Python list]
def insertion_sort_array(list_to_sort):
    n = len(list_to_sort)
    for i in range(n):
        el = list_to_sort[i]
        k = i - 1
        while el < list_to_sort[k] and k > - 1:
            list_to_sort[k + 1] = list_to_sort[k]
            list_to_sort[k] = el
            k -= 1


# selection sort for array [Python list]
def selection_sort_array(list_to_sort):
    n = len(list_to_sort)
    for i in range(n - 1):
        smallest = list_to_sort[i]
        position = i
        for j in range(i + 1, n):
            if list_to_sort[j] < smallest:
                smallest = list_to_sort[j]
                position = j
        list_to_sort[position], list_to_sort[i] = list_to_sort[i], smallest


# bubble sort for array [Python list]
def bubble_sort_array(list_to_sort):
    n = len(list_to_sort)
    while True:
        were_changes = False
        for i in range(n - 1):
            if list_to_sort[i] > list_to_sort[i + 1]:
                were_changes = True
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
        if were_changes is False:
            break


def selection_sort_list(list_to_sort):
    if list_to_sort is None or list_to_sort.next is None:
        return list_to_sort
    guardian = Node(0, list_to_sort)
    list_to_sort_prev = guardian
    while list_to_sort.next is not None:
        r = list_to_sort.next
        prev = list_to_sort
        smallest = list_to_sort
        smallest_prev = list_to_sort_prev
        while r is not None:
            if r.val < smallest.val:
                smallest_prev = prev
                smallest = r
            prev = r
            r = r.next
        list_to_sort_prev.next, smallest_prev.next = smallest, list_to_sort
        list_to_sort.next, smallest.next = smallest.next, list_to_sort.next
        list_to_sort_prev = smallest
        list_to_sort = smallest.next
    return guardian.next


def bubble_sort_list(list_to_sort):
    if list_to_sort is None or list_to_sort.next is None:
        return list_to_sort
    guardian = Node(0, list_to_sort)
    while True:
        was_changed = False
        r = guardian.next
        prev = guardian
        while r.next is not None:
            if r.val > r.next.val:
                was_changed = True
                temp = r.next
                r.next = temp.next
                prev.next = temp
                temp.next = r
                prev = temp
            else:
                prev = r
                r = r.next
        if was_changed is False:
            return guardian.next
