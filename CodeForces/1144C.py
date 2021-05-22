def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    if p < r:
        q = partition(tab, p, r)
        quicksort(tab, p, q - 1)
        quicksort(tab, q + 1, r)


def try_dividing(array):
    n = len(array)
    # sort array
    quicksort(array, 0, n - 1)
    # check if array can be divide into two arrays (cant do that if there more than two identical numbers)
    i = 0
    overall_count = 0
    while i < n:
        count = 1
        temp = array[i]
        i += 1
        while i < n and array[i] == temp:
            i += 1
            count += 1
            overall_count += 1
            if count > 2:
                return False, [], []

    if overall_count == 0:
        return True, array, []

    rising = [0] * (n - overall_count)
    decreasing = [0] * overall_count
    i = 0
    j = 0
    overall_count -= 1
    while i < n:
        rising[j] = array[i]
        j += 1
        if i < n - 1 and array[i] == array[i + 1]:
            decreasing[overall_count] = array[i + 1]
            i += 1
            overall_count -= 1
        i += 1
    return True, rising, decreasing


def take_input():
    x = int(input())
    array = input().split(sep=" ")
    for i in range(x):
        array[i] = int(array[i])
    return array


def give_output(success, rising, decreasing):
    if not success:
        print("NO")
    else:
        print("YES")
        print(len(rising))
        for element in rising:
            print(element, end=" ")
        print()
        print(len(decreasing))
        for element in decreasing:
            print(element, end=" ")
        print()


if __name__ == "__main__":
    array_to_test = take_input()
    was_successful, r, d = try_dividing(array_to_test)
    give_output(was_successful, r, d)
