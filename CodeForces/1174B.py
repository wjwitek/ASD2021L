from random import randint


def check_for_parity(tab):
    parity = tab[0] % 2
    for i in range(1, len(tab)):
        if tab[i] % 2 != parity:
            return False
    return True


def quicker_partition(tab, p, r):
    x = tab[r]
    i = p - 1
    k = r - 1
    j = p
    while j <= k:
        if tab[j] < x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
            j += 1
        elif tab[j] == x:
            tab[k], tab[j] = tab[j], tab[k]
            k -= 1
        else:
            j += 1
    for l in range(r - k):
        tab[l + i + 1], tab[k + 1 + l] = tab[k + 1 + l], tab[l + i + 1]
    return i, i + r - k + 1


def quicker_sort(tab, p, r):
    while p < r:
        left, right = quicker_partition(tab, p, r)
        if left - p < r - right:
            quicker_sort(tab, p, left)
            p = right
        else:
            quicker_sort(tab, right, r)
            r = left

def print_output(arr):
    for el in arr:
        print(el, end=" ")
    print()


if __name__ == "__main__":
    length = int(input())
    array = list(map(int, input().split()))
    if check_for_parity(array):
        print_output(array)
    else:
        quicker_sort(array, 0, length - 1)
        print_output(array)
