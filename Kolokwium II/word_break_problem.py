"""
Word Break Problem: Given a string and a dictionary of words determine if the string can be segmented into a
space-separated sequence of one or more dictionary words.

f(i, j) = can substring from i to j included be separated into words
"""


def word_break(dictionary, string_to_div):
    n = len(string_to_div)
    divisions = [[False for _ in range(n)] for _ in range(n)]

    def check(i, j):
        if divisions[i][j]:
            return True
        if i == j:
            return string_to_div[i] in dictionary
        if string_to_div[i:j+1] in dictionary:
            divisions[i][j] = True
            return True
        for k in range(j - i):
            if check(i, i + k) and check(i + k + 1, j):
                divisions[i][j] = True
                return True
        return False

    return check(0, n-1)


test_dict = {'this', 'th', 'is', 'famous', 'Word', 'break', 'b', 'r', 'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'problem'}
test_string = "Wordbreakproblems"

print(word_break(test_dict, test_string))
