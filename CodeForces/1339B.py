"""
steps:
-> sort array
-> find median
-> median (i) goes first than i + 1, i - 1, i + 2, i - 2 etc.
"""
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



def sort_out_array(tab):
    quicker_sort(tab, 0, len(tab) - 1)
    i = (len(tab) - 1) // 2
    print(tab[i], end=" ")
    j = i - 1
    k = i + 1
    while j > -1 or k < len(tab):
        if k < len(tab):
            print(tab[k], end=" ")
            k += 1
        if j > -1:
            print(tab[j], end=" ")
            j -= 1
    print()


def get_input():
    number_of_problems = int(input())
    arrays = [0] * number_of_problems
    for i in range(number_of_problems):
        length_of_array = int(input())
        temp = input().split(sep=" ")
        for j in range(length_of_array):
            temp[j] = int(temp[j])
        arrays[i] = temp
    return arrays


if __name__ == "__main__":
    arrays_to_sort = get_input()
    for array in arrays_to_sort:
        sort_out_array(array)
