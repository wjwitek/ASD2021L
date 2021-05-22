from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None


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


def qsort( L ):
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


def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")


seed(42)

n = 10
T = [2, 3, 11, 7, 5, 23, 17, 19, 13, 29, 41, 37, 31, 89, 47, 53, 59, 61, 67, 71, 73, 43, 83, 79]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")


