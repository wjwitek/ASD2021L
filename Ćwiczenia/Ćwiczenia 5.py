from random import randint


# problem najdłuższego rosnącego podciągu w czasie O(nlog(n))
def mod_binary_search(array, start, end, key, tails_index, key_index, parents):
    while end - start > 1:
        mid = start + (end - start) // 2
        if array[mid] > key:
            end = mid
        else:
            start = mid
    array[end] = key
    parents[key_index] = parents[tails_index[end]]
    tails_index[end] = key_index


def print_sequence_l(index, parents, array):
    if parents[index] != -1:
        print_sequence_l(parents[index], parents, array)
    print(array[index], end=" ")


def longest_subsequence(array):
    n = len(array)
    tails = [-1] * n
    tails_index = [-1] * n
    parents = [-1] * n
    tails[0] = array[0]
    tails_index[0] = 0
    last = 0
    for i in range(1, n):
        if array[i] < tails[0]:
            tails[0] = array[i]
            tails_index[0] = i
            parents[i] = -2
        elif array[i] > tails[last]:
            tails[last + 1] = array[i]
            parents[i] = tails_index[last]
            last += 1
            tails_index[last] = i
        else:
            mod_binary_search(tails, 0, last, array[i], tails_index, i, parents)
    print_sequence_l(tails_index[last], parents, array)
    print()
    return last + 1


test = [0, 8, 4, 12, 2, 10, 6, 9, 5, 13, 3, 11, 7, 1, 15, 2]
print(longest_subsequence(test))


def print_sequence(array, i):
    if array[i][1] == -2:
        print(i, end=" ")
    else:
        print_sequence(array, array[i][1])
        print(i - array[i][1], end=" ")


# znaleźć czy istnieje podciąg sumujący się do t, O(t*n)
def subsequence_of_sum(array, t):
    n = len(array)
    sums = [[False, -1] for _ in range(t + 1)]
    last_false = 0
    for i in range(n):
        if array[i] > t:
            continue
        for j in range(last_false):
            if sums[j][0] and j + array[i] <= t:
                sums[j + array[i]][0] = True
                sums[j + array[i]][1] = j
                if j + array[i] >= last_false:
                    last_false = j + array[i] + 1
        sums[array[i]][0] = True
        sums[array[i]][1] = -2
        if array[i] >= last_false:
            last_false = array[i] + 1
        if sums[t][0]:
            print_sequence(sums, t)
            print()
            return
    print("Not found")


# test = [5, 7, 3, 8, 1]
# subsequence_of_sum(test, 2000)


# problem plecakowy w czasie O(n*suma_zysków)
def knapsack_mod(weight, value, max_weight):
    n = len(weight)
    sum_of_values = 0
    furthest_value = 0
    for v in value:
        sum_of_values += v
    sums = [None] * n
    for i in range(n):
        sums[i] = [0] * (sum_of_values + 1)
    if weight[0] <= max_weight:
        furthest_value = value[0]
        for i in range(value[0] + 1):
            sums[0][i] = weight[0]
    for i in range(1, n):
        for j in range(value[i]):
            sums[i][j] = sums[i - 1][j]
        for j in range(value[i], furthest_value + value[i] + 1):
            if sums[i - 1][j] != 0:
                if sums[i - 1][j - value[i]] + weight[i] < sums[i - 1][j]:
                    sums[i][j] = sums[i - 1][j - value[i]] + weight[i]
                else:
                    sums[i][j] = sums[i - 1][j]
            elif sums[i - 1][j - value[i]] + weight[i] <= max_weight:
                sums[i][j] = sums[i - 1][j - value[i]] + weight[i]
                furthest_value = j
            else:
                break
    return furthest_value


# W  lesie  znajduje  się  n  drzew  stojących  w  jednej  linii.  Każde  drzewo  posiada  określoną  wartość,  która
# należy  traktować  jako  zysk  po  jego  wycięciu.  Nie  możemy  wyciąć  więcej  niż  dwóch  drzew  pod  rząd. Proszę
# zaimplementować funkcję pozwalającą określić które drzewa należy wyciąć, aby sumaryczny zysk był jak największy.
def choose_trees(values):
    n = len(values)
    sums = [[0, 0] for _ in range(n)]
    sums[0] = [values[0], 1]
    sums[1] = [values[0] + values[1], 2]
    # find treed and sum
    for i in range(2, n):
        if sums[i - 1][1] < 2:
            sums[i][0] = sums[i - 1][0] + values[i]
            sums[i][1] = sums[i - 1][1] + 1
        else:
            sums[i][0] = sums[i - 1][0]
            sums[i][1] = 0
            if sums[i][0] < sums[i - 2][0] + values[i]:
                sums[i][0] = sums[i - 2][0] + values[i]
                sums[i][1] = 1
            if sums[i][0] < sums[i - 1][0] - values[i - 2] + values[i]:
                sums[i][0] = sums[i - 1][0] - values[i - 2] + values[i]
                sums[i][1] = 2
    # print values and indexes of trees
    k = n - 1
    while k > -1:
        if sums[k][1] == 2:
            print((k, values[k]), end=" ")
            print((k - 1, values[k - 1]), end=" ")
            k -= 3
        elif sums[k][1] == 1:
            print((k, values[k]), end=" ")
            k -= 2
        else:
            k -= 1
    print()


# Tablica N[t] dostępnych nominałów, S - kwota do wydania. Obliczyć minimalną liczbę monet do wydania S.

