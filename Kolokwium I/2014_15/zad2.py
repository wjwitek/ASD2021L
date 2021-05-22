from node_functions import Node
"""
Dane są następujące struktury: struct Node{Node* next; int val;}; struct TwoLists{Node* even; Node* odd;};
Napisać funkcję: TwoLists split(Node* list); Funkcja rozdziela listę na dwie: jedną zawierającą liczby parzyste
i drugą zawierającą liczby nieparzyste. Listy nie zawierają wartowników.
"""


def split(first):
    even = Node("even")
    odd = Node("odd")
    even_pivot, odd_pivot = even, odd
    while first is not None:
        if first.val % 2 == 0:
            even_pivot.next = first
            even_pivot = even_pivot.next
        else:
            odd_pivot.next = first
            odd_pivot = odd_pivot.next
        first = first.next
    even_pivot.next, odd_pivot.next = None, None
    return even.next, odd.next
