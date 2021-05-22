"""
Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
struct Node{Node* next; double value;}
Proszę zaimplementować funkcjęvoid Sort( Node* list ), która otrzymuje na wejściu listę liczb rzeczywistych
(z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym naprzedziale [0,10) i sortuje jej zawartość
w kolejności niemalejącej. Funkcja powinna być możliwiejak najszybsza (biorąc pod uwagę warunki zadania).
Proszę oszacować złożoność zaimplementowanej funkcji
"""
from node_functions import Node
from node_functions import tab_to_list
from node_functions import list_to_str


# algorithm: bucket sort (ten buckets), average time complexity: O(n+10)
def selection_sort(list_to_sort):
    if list_to_sort is None or list_to_sort.next is None:
        return list_to_sort
    guardian = list_to_sort
    list_to_sort = list_to_sort.next
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
    return list_to_sort


def bucket_sort(first):
    guardians = [Node(i) for i in range(10)]
    pivots = [guardians[i] for i in range(10)]
    # divide elements of list into buckets
    while first.next is not None:
        index = int(first.next.val % 10)
        pivots[index].next = first.next
        first.next = first.next.next
        pivots[index] = pivots[index].next
        pivots[index].next = None
    # sort elements inside buckets
    for i in range(10):
        if guardians[i].next is None:
            continue
        pivots[i] = selection_sort(guardians[i])
    # add elements from bucket back to first
    r = first
    for i in range(10):
        if guardians[i].next is None:
            continue
        r.next = guardians[i].next
        r = pivots[i]


test = [4, 3, 2, 7, 2, 8, 9, 1]
test_first = Node("!")
test_first.next = tab_to_list(test)
print(list_to_str(test_first))
bucket_sort(test_first)
print(list_to_str(test_first))
"""test = [2, 2, 4]
f = Node("!")
f.next = tab_to_list(test)
print(list_to_str(selection_sort(f)))
print(list_to_str(f))
"""