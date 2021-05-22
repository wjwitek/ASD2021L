# finding substring of maximum sum

def find_on_cross(tab, beg, end, mid_l, mid_r):
    biggest_sum, current_sum = 0, 0
    for i in range(mid_l, beg - 1, -1):
        current_sum += tab[i]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
    current_sum, biggest_sum_2 = 0, 0
    for i in range(mid_r, end + 1):
        current_sum += tab[i]
        if current_sum > biggest_sum_2:
            biggest_sum_2 = current_sum
    return biggest_sum + biggest_sum_2


def search_for_substring(tab, beg, end):
    if end - beg + 1 == 0:
        return 0
    if beg == end:
        return max(0, tab[beg])
    else:
        sum1 = search_for_substring(tab, beg, beg + (end - beg) // 2)
        sum2 = search_for_substring(tab, beg + (end - beg) // 2 + 1, end)
        sum3 = find_on_cross(tab, beg, end, beg + (end - beg) // 2, beg + (end - beg) // 2 + 1)
        return max(sum1, sum2, sum3)
