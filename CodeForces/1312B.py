# quicksort but sorting from biggest to smallest
def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] >= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    if p < r:
        q = partition(tab, p, r)
        quicksort(tab, p, q - 1)
        quicksort(tab, q + 1, r)


def take_input():
    number_of_cases = int(input())
    arrays = [0] * number_of_cases
    for i in range(number_of_cases):
        n = int(input())
        temp = input().split(sep=" ")
        for j in range(n):
            temp[j] = int(temp[j])
        arrays[i] = temp
    return arrays


def sort_input(arrays):
    for array in arrays:
        quicksort(array, 0, len(array) - 1)


def print_output(arrays):
    for array in arrays:
        for element in array:
            print(element, end=" ")
        print()


if __name__ == "__main__":
    arrays = take_input()
    sort_input(arrays)
    print_output(arrays)
