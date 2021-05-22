class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None


def tab_to_list(tab):
    head = Node("!")
    r = head
    for i in tab:
        r.next = Node(i)
        r = r.next
    return head.next


def print_list(first):
    while first:
        print(first.value, end="")
        first = first.next
    print()


# merge sort for linked lists
def merge(first1, first2):
    new_list = Node("!")
    tail = new_list
    while first1 is not None and first2 is not None:
        if first1.value < first2.value:
            tail.next = first1
            first1 = first1.next
        else:
            tail.next = first2
            first2 = first2.next
        tail = tail.next
    if first1 is not None:
        tail.next = first1
    if first2 is not None:
        tail.next = first2
    return new_list.next


def merge_sort(first):
    if not first or not first.next:
        return first

    mid = first
    last = first

    while last.next and last.next.next:
        mid = mid.next
        last = last.next.next

    right_head = mid.next
    mid.next = None
    left = merge_sort(first)
    right = merge_sort(right_head)
    return merge(left, right)


# use merge sort to count inversions in an array
def modified_merge(T, l, m, r):
    inversions = 0
    new = [0 for _ in range(r - l + 1)]
    idx = 0
    i = l
    j = m + 1
    while i <= m and j <= r:
        if T[j] > T[i]:
            new[idx] = T[i]
            i += 1
        else:
            inversions += m - i + 1
            new[idx] = T[j]
            j += 1
        idx += 1

    while i <= m:
        new[idx] = T[i]
        i += 1
        idx += 1
    while j <= r:
        inversions += m - i + 1
        new[idx] = T[j]
        j += 1
        idx += 1

    idx = 0
    for i in range(l, r+1):
        T[i] = new[idx]
        idx += 1
    return inversions


def inversion_count(T, l, r):
    inversions = 0
    if l < r:
        m = (r + l) // 2
        inversions += inversion_count(T, l, m)
        inversions += inversion_count(T, m + 1, r)
        inversions += modified_merge(T, l, m, r)
    return inversions


def find_leader(tab):
    leader = -1
    counter = 0
    for i in range(len(tab)):
        if counter == 0:
            leader = tab[i]
            counter = 1
        elif leader == tab[i]:
            counter += 1
        else:
            counter -= 1
    if counter > 0:
        counter = 0
        for i in range(len(tab)):
            if tab[i] == leader:
                counter += 1
        if counter > len(tab) // 2:
            return True
    return False


# przedziały zawierające się - segregujemy względem lewej, w nowej tablicy względem prawej, a potem
# szukamy tego przedziały który w pierwszym szeregu jest jak najbardziej z lewej a w drugim jak
# najbardziej z prawej


test = [2, 2, 2, 4, 5, 6]
print(find_leader(test))