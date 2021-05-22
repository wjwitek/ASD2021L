"""
Given an M x N matrix, calculate the maximum sum submatrix of size k x k in it in O(M x N) time.
"""


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


def sum_submatrix(partial_sums, p1, q1, p2, q2):
    if p1 == q1 == 0:
        return partial_sums[p2][q2]
    elif p1 == 0:
        return partial_sums[p2][q2] - partial_sums[p2][q1 - 1]
    elif q1 == 0:
        return partial_sums[p2][q2] - partial_sums[p1 - 1][q2]
    else:
        return partial_sums[p2][q2] - partial_sums[p2][q1 - 1] - partial_sums[p1 - 1][q2] + partial_sums[p1 - 1][q2 - 1]


def biggest_submatrix(matrix, k):
    partial_sums = submatrix(matrix)
    n = len(matrix)
    m = len(matrix[0])
    maximum = 0
    for i in range(n - k):
        for j in range(m - k):
            temp = sum_submatrix(partial_sums, i, j, i + k - 1, j + k - 1)
            if temp> maximum:
                maximum = temp
    return maximum

