"""
Wildcard Pattern Matching: Given a string and a patterns containing wildcard characters: * and ?, where ? can match to
any single character in the string and * can match to any number of characters including zero characters, design an
efficient algorithm to find if the pattern matchers with the complete string or not.
"""


def match(complete, pattern):
    n = len(complete)
    m = len(pattern)
    index = 0
    matrix = [[False for _ in range(n)] for _ in range(m)]
    i = 0
    while i < m and pattern[i] == '*':
        i += 1
    if i == m:
        return True
    if i != 0:
        if pattern[i] == '?':
            for j in range(n):
                matrix[i][j] = True
        else:
            for j in range(n):
                if complete[j] == pattern[i]:
                    matrix[i][j] = True
    else:
        if pattern[0] == '?':
            matrix[0][0] = True
        elif complete[0] == pattern[0]:
            matrix[0][0] = True
        else:
            return False
    index += 1
    i += 1
    while i < m:
        if pattern[i] == '*':
            for j in range(index, n):
                matrix[i][j] = True
        elif pattern[i] == '?':
            for j in range(index, n):
                if matrix[i - 1][j - 1]:
                    matrix[i][j] = True
            index += 1
        else:
            flag = True
            for j in range(index, n):
                if matrix[i - 1][j - 1] and complete[j] == pattern[i]:
                    flag = False
                    matrix[i][j] = True
            if flag:
                return False
            index += 1
        i += 1
    return matrix[m - 1][n - 1]


def execute():
    c = input()
    p = input()
    return match(c, p)


print(execute())
