"""
Given an M x N matrix and two coordinates (p, q) and (r, s) representing top-left and bottom-right coordinates of a
submatrix  of it, calculate the sum of all elements present in the submatrix. We will do m such operations, so one
should require O(1) time.
"""


from random import randint


def submatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    partial_sums = [[-1 for _ in range(m)] for _ in range(n)]
    partial_sums[0][0] = matrix[0][0]
    for i in range(1, n):
        partial_sums[i][0] = partial_sums[i - 1][0] + matrix[i][0]
    for i in range(1, m):
        partial_sums[0][i] = partial_sums[0][i - 1] + matrix[0][i]
    for i in range(1, n):
        for j in range(1, m):
            partial_sums[i][j] = partial_sums[i - 1][j] + partial_sums[i][j - 1] \
                                 - partial_sums[i - 1][j - 1] + matrix[i][j]
    return partial_sums


def wrapper(matrix):
    partial_sums = submatrix(matrix)
    p1, q1, p2, q2 = [int(x) for x in input("coords: ").split(sep=" ")]
    while p1 != -1:
        if p1 == q1 == 0:
            print(partial_sums[p2][q2])
        elif p1 == 0:
            print(partial_sums[p2][q2] - partial_sums[p2][q1 - 1])
        elif q1 == 0:
            print(partial_sums[p2][q2] - partial_sums[p1 - 1][q2])
        else:
            print(partial_sums[p2][q2] - partial_sums[p2][q1 - 1]
                  - partial_sums[p1 - 1][q2] + partial_sums[p1 - 1][q2 - 1])
        p1, q1, p2, q2 = [int(x) for x in input("coords: ").split(sep=" ")]


if __name__ == "__main__":
    random_matrix = [[randint(-100, 100) for _ in range(5)] for _ in range(6)]
    for row in random_matrix:
        print(row)
    wrapper(random_matrix)
