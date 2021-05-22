from math import sqrt
from random import randint


# partition take element with index r and find its place in array
def partition(tab, p, r, idx):
    x = abs(tab[r][idx])
    i = p - 1
    for j in range(p, r):
        if abs(tab[j][idx]) <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r, idx):
    if p < r:
        q = partition(tab, p, r, idx)
        quicksort(tab, p, q - 1, idx)
        quicksort(tab, q + 1, r, idx)


# very similar algorithm to above but with random r
def randomized_partition(tab, p, r, idx):
    i = randint(p, r)
    tab[r], tab[i] = tab[i], tab[r]
    return partition(tab, p, r, idx)


def randomized_quicksort(tab, p, r, idx):
    if p < r:
        q = randomized_partition(tab, p, r, idx)
        quicksort(tab, p, q - 1, idx)
        quicksort(tab, q + 1, r, idx)


def sort(miners, diamonds):
    randomized_quicksort(miners, 0, len(miners) - 1, 1)
    randomized_quicksort(diamonds, 0, len(diamonds) - 1, 0)


def calculate_energy(miner, diamond):
    return sqrt(diamond[0]**2 + miner[1]**2)


def find_energy(miners, diamonds):
    n = len(miners)
    sort(miners, diamonds)
    energy = 0
    for i in range(n):
        energy += calculate_energy(miners[i], diamonds[i])
    return energy


def get_input():
    number_of_cases = int(input())
    cases = []
    for i in range(number_of_cases):
        n = int(input())
        miners, diamonds = [], []
        for j in range(2 * n):
            temp = input().split(sep=" ")
            if temp[0] == '0':
                miners.append((0, int(temp[1])))
            else:
                diamonds.append((int(temp[0]), 0))
        cases.append((miners, diamonds))
    return cases


if __name__ == "__main__":
    my_cases = get_input()
    for case in my_cases:
        my_miners, my_diamonds = case
        print(find_energy(my_miners, my_diamonds))
