"""
Write an efficient algorithm to check if a given string is k-palindrome o not. A string is k-palindrome if it becomes
a palindrome on removing at most k characters from it.
"""


def palindrome(text, k):
    copy = text[::-1]
    n = len(text)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                matrix[i][j] = max(i, j)
            elif text[i - 1] == copy[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[n][n] <= 2 * k
