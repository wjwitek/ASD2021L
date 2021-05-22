# returns array of matching keys
def binary_search(tab, idx, target, l, r):
    n = len(tab)
    while l <= r:
        mid = l + (r - l) // 2
        if tab[mid][idx] == target:
            left = mid - 1
            while left > 0 and tab[left][idx] == target:
                left -= 1
            right = mid + 1
            while right < n and tab[right][idx] == target:
                right += 1
            return left, right
        elif tab[mid][idx] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1, -1
