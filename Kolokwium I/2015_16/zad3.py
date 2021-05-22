from node_functions import Node
"""
Dana jest struktura Node opisująca listę jednokierunkową: struct Node{Node * next; int value;};
Proszę zaimplementować funkcjęNode* fixSortedList( Node* L ), która otrzymuje na wejściu listę jednokierunkową
bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że powstała z listy
posortowanej przez zmianę jednego losowo wybranego elementu na losową wartość. Funkcja powinna przepiąć
elementy listy tak, by lista stała się posortowana i zwrócić wskaźnik do głowy tej listy. Można założyć,
że wszystkie liczby na liście są różne i że lista ma conajmniej dwa elementy. Funkcja powinna działać
w czasie liniowym względem długości listy wejściowej.
"""


def find_wrong_one(guardian):
    first = guardian.next
    if first.val > first.next.val:
        # case when first element was changed
        # (or second, but those two cases can't be differentiated without seeing original list)
        guardian.next = first.next
        return first
    a, b, c = first, first.next, first.next.next
    while c is not None:
        if a.val < b.val < c.val:
            # nothing is wrong, move forward
            a = a.next
            b = b.next
            c = c.next
        else:
            # check which element is wrong
            if a.val < c.val:
                a.next = c
                return b
            else:
                b.next = c.next
                return c
    return None # means that changing value has not broken order


def find_right_place(guardian, element):
    pivot = guardian.next
    prev = guardian
    while pivot is not None and pivot.val < element.val:
        prev = pivot
        pivot = pivot.next
    prev.next = element
    element.next = pivot


def fix_sorted_list(first):
    guardian = Node("!")
    guardian.next = first
    wrong_node = find_wrong_one(guardian)
    find_right_place(guardian, wrong_node)
    return guardian.next
