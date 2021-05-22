# implement selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        index = i
        for j in range(i, n):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]


# define linked list class, printing it, tab-to-list and insertion sort for linked list
class Node:
    def __init__(self, new_val=None, next_node=None):
        self.val = new_val
        self.next = next_node

    def __str__(self):
        return str(self.val) + " -> " + str(self.next)


def tab_to_list(tab):
    head = Node("!")
    r = head
    for i in tab:
        r.next = Node(i)
        r = r.next
    return head


def insertion_sort(head):
    # rewrite elements to new list - just moving pointers anyway and it's much easier to do
    pivot = head.next
    new_head = Node("!")
    while pivot is not None:
        head.next = head.next.next
        # search where to put pivot
        r, prev = new_head.next, new_head
        while r is not None and pivot.val > r.val:
            prev, r = r, r.next
        prev.next = pivot
        pivot.next = r
        pivot = head.next
    return new_head


# implement bubble sort for linked list
def bubble_sort(head):
    if head is None or head.next is None:
        return head
    mid = head.next
    front = mid.next

    while True:
        was_changed = False
        while front is not None:
            if mid.val > front.val:
                front.val, mid.val = mid.val, front.val
                was_changed = True
            back, mid, front = mid, front, front.next
        if was_changed is False:
            break
    return head


def maxi_mini(arr):
    maxi = mini = arr[0]

    for i in range(len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]
        elif arr[i] < mini:
            mini = arr[i]
    return maxi, mini


def search_for_sum(arr, x):
    n = len(arr)
    i, j = 0, n - 1
    while i < j:
        temp = arr[i] + arr[j]
        if temp > x:
            j -= 1
        elif temp < x:
            i += 1
        else:
            return i, j
    return -1, -1


test = [2, 4, 5, 6, 12]
print(search_for_sum(test, 34))