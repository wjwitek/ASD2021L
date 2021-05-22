"""
Given a square matrix, print the maximum length sequence in it. A snake sequence is defined as a sequence of numbers
where each new number, which can only be located to the right of down of current number, is either plus or minus one.
"""


def find_snake(grid):
    n = len(grid)
    solutions = [[1] * n for _ in range(n)]
    solutions[n - 1][n - 1] = 1
    for i in range(n - 2, -1, -1):
        if abs(grid[n - 1][i] - grid[n - 1][i + 1]) == 1:
            solutions[n - 1][i] = solutions[n - 1][i + 1] + 1
        if abs(grid[i][n - 1] - grid[i + 1][n - 1]) == 1:
            solutions[i][n - 1] = solutions[i + 1][n - 1] + 1
    current_maximum = 1
    for i in range(n - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            # check if next move could be down
            if abs(grid[i][j] - grid[i + 1][j]) == 1:
                solutions[i][j] = solutions[i + 1][j] + 1
            # check if next move could be right
            if abs(grid[i][j] - grid[i][j + 1]) == 1 and solutions[i][j + 1] + 1 > solutions[i][j]:
                solutions[i][j] = solutions[i][j + 1] + 1
            if solutions[i][j] > current_maximum:
                current_maximum = solutions[i][j]
    for row in solutions:
        print(row)
    return current_maximum


if __name__ == '__main__':
    matrix = [
        [7, 5, 2, 3, 1],
        [3, 4, 1, 4, 4],
        [1, 5, 6, 7, 8],
        [3, 4, 5, 8, 9],
        [3, 2, 2, 7, 6]
    ]

    path = find_snake(matrix)
    print("The maximum length snake sequence:", path)
