# Weronika Witek
from zad2testy import runtests
from math import ceil, log2
"""
Funkcja ma dwa "tryby", dla k > log(n) jest to po prostu quicker_sort i dla takich danych ma złożoność O(nlog(n)). Natomiast dla 
k <= log(n) funkcja najpierw selection sortem sortuje k + 1 pierwszych elementów, a póżniej dla każdego kolejnego elementu znajduje odpowiednie 
miejsce w liście szukając w zakresie od wskaźnika start.next (który przesuwa się o 1 w prawo dla każdego kolejnego elementu) do tego elementu, a więc zawsze
w zakresie o szerokości k. Jest to możliwe dlatego, że dzięki k-chaotyczności sortując najpierw selection sortem, a potem tak wstawiając elementy wiemy zawsze, że liczba
pod wskażnikiem start jest już na swoim miejscu. Daje to złożoność: O(k*n) (dlatego jest to algorytm "opłacalny" tylko dla k <= log(n)).
dla k=O(1) - złożonośc czasowa O(n)
dla k=O(logn) - złożoność czasowa O(nlog(n))
dla k=O(n) - złożoność czasowa O(log(n))
"""


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def k_sort(first, k):
    guardian = Node()
    guardian.next = first
    r = first
    prev_r = guardian
    for i in range(k+1):
        mini = r
        mini_prev = prev_r
        prev_p = r
        p = r.next
        for j in range(i + 1, k+1):
            if p.val < mini.val:
                mini = p
                mini_prev = prev_p
            prev_p = p
            p = p.next
        if mini == r:
            prev_r = r
            r = r.next
        else:
            prev_r.next, mini_prev.next = mini, r
            mini.next, r.next = r.next, mini.next
            r = mini.next
            prev_r = mini
    start = guardian.next
    while r is not None:
        q = start.next
        q_prev = start
        while r.val >= q.val and q is not r:
            q_prev = q
            q = q.next
        if r.val < q.val:
            q_prev.next = r
            prev_r.next = r.next
            r.next = q
            r = prev_r.next
        else:
            prev_r = r
            r = r.next
        start = start.next
    return guardian.next

def partition(first, last, last_next, first_prev):
    # returns elements: one before those equal to pivot, one after, new element that is before last_next, last element of those equal
    equal, smaller, greater = Node(), Node(), Node()
    equal_pivot, smaller_pivot, greater_pivot = equal, smaller, greater
    while first != last:
        if first.val == last.val:
            equal_pivot.next = first
            equal_pivot = equal_pivot.next
        elif first.val < last.val:
            smaller_pivot.next = first
            smaller_pivot = smaller_pivot.next
        else:
            greater_pivot.next = first
            greater_pivot = greater_pivot.next
        first = first.next
    # add last to equals
    equal_pivot.next = last
    equal_pivot = equal_pivot.next
    # rejoin list and give values to variables that are returned
    if smaller.next is None:
        first_prev.next = equal.next
        before = first_prev
    else:
        first_prev.next = smaller.next
        smaller_pivot.next = equal.next
        before = smaller_pivot
    if greater.next is None:
        equal_pivot.next = last_next
        after = last_next
        new_end = equal_pivot
    else:
        equal_pivot.next = greater.next
        greater_pivot.next = last_next
        after = greater.next
        new_end = greater_pivot
    after_prev = equal_pivot
    return before, after, new_end, after_prev


def check_if_earlier(q, r):
    while q is not None:
        if q.next == r:
            return True
        q = q.next
    return False


def main_quicksort(q, r, q_prev):
    if q.val == "!":
        q = q.next
    if check_if_earlier(q, r):
        before, after, new_end, after_prev = partition(q, r, r.next, q_prev)
        main_quicksort(q_prev.next, before, q_prev) # using q_prev, new_end and after_prev because q and r are moved in partition
        main_quicksort(after, new_end, after_prev)


def quicker_sort(first):
    if first is None or first.next is None:
        return first
    # find last element of list
    last = first
    while last.next is not None:
        last = last.next
    # add temporary guardian at the beggining
    guardian = Node()
    guardian.val, guardian.next = "!", first
    main_quicksort(first, last, guardian)
    return guardian.next


def SortH(p,k):
    n = 0
    # count number of elements in list
    r = p
    while r is not None:
        n += 1
        r = r.next
    if k <= ceil(log2(n)):
        p = k_sort(p, k)
    else:
        p = quicker_sort(p)
    return p

runtests( SortH ) 