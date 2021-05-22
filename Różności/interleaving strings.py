"""
Given three strings, return true it the third string is interleaving the first and second strings, i.e., it is formed
from all characters of the first and second string, and the order of characters is preserved.
"""


def check_strings(first, second, third):
    m, n = len(first), len(second)
    if m + n != len(third):
        return False
    solution = [[False] * (m + 1) for _ in range(n + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                solution[i][j] = True
            elif first[i - 1] == second[j - 1] == third[i + j - 1]:
                solution[i][j] = solution[i - 1][j] or solution[i][j - 1]
            elif first[i - 1] == third[i + j - 1]:
                solution[i][j] = solution[i - 1][j]
            elif second[j - 1] == third[i + j - 1]:
                solution[i][j] = solution[i][j - 1]
            else:
                return False
    return solution[m][n]
