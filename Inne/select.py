from quicksort import randomized_partition


def quick_select(tab, start, end, i):
    if start >= end:
        return tab[start]
    q = randomized_partition(tab, start, end)
    k = q - start + 1
    if k == i:
        return tab[q]
    elif i < k:
        return quick_select(tab, start, q - 1, i)
    else:
        return quick_select(tab, q + 1, end, i - k)
