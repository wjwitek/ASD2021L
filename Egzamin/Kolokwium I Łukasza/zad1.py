from zad1testy import runtests
import math

null = None

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


def insert(head, elem):
    elem = Node(elem)
    cp, cp2 = head, head.next
    while cp2 != null and elem.val > cp2.val:
        cp, cp2 = cp2, cp2.next
    cp.next = elem
    elem.next = cp2


def zlacz(tab, nowa, n):
    idx = 0
    for i in range(n):
        if tab[i].next is not None:
            nowa[idx] = tab[i].next.val
            idx += 1
            cp = tab[i].next.next
            while cp is not None:
                nowa[idx] = cp.val
                cp = cp.next
                idx += 1


                 
    
# co moge poweidziec O(n) wystarczy wziac logarytm i ez
def fast_sort(tab, a):
    # tu prosze wpisac implementacje
    n = len(tab)
    buckets = [Node("!") for _ in range(n)]
    for x in tab:
        # to log(x,a)*n dziala dla danych miedzy 0 a 1
        # dla innych to jebnie
        insert(buckets[int(math.log(x,a) * n)], x)
    zlacz(buckets, tab, n)
    return tab



runtests( fast_sort )
