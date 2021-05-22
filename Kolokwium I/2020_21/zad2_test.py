"""
Założenie: k <= n
"""
from node_functions import Node, tab_to_list, list_to_str
from math import ceil, log2


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
    if first.value == last.value:
      equal_pivot.next = first
      equal_pivot = equal_pivot.next
    elif first.value < last.value:
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
  if check_if_earlier(q, r):
    before, after, new_end, after_prev = partition(q, r, r.next, q_prev)
    main_quicksort(q_prev.next, before, q_prev) # using q_prev, new_end and after_prev because q and r are moved in partition
    main_quicksort(after, new_end, after_prev)


def quick_sort( L ):
  if L is None or L.next is None:
    return L
  # find last element of list
  last = L
  while last.next is not None:
    last = last.next
  # add temporary guardian at the beggining
  first = Node()
  first.value, first.next = "!", L
  main_quicksort(L, last, first)
  L = first.next
  return L



def main_sort(first, k):
    n = 0
    # count number of elements in list
    r = first
    while r is not None:
        n += 1
        r = r.next
    if k <= ceil(log2(n)):
        first = k_sort(first, k)
    else:
        first = quick_sort(first)
    return first
