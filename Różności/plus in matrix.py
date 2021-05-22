"""
Given a square matrix of 0's and 1's, calculate the size of the largest plus formed by 1's.
"""


def search(grid):
    n = len(grid)
    to_left = [[0] * n for _ in range(n)]
    to_right = [[0] * n for _ in range(n)]
    up = [[0] * n for _ in range(n)]
    down = [[0] * n for _ in range(n)]
    for i in range(n):
        to_left[i][0] = grid[i][0]
        to_right[i][n - 1] = grid[i][n - 1]
        up[0][i] = grid[0][i]
        down[n - 1][i] = grid[n - 1][i]
    for i in range(n):
        for j in range(1, n):
            to_left[i][j] = to_left[i][j - 1] + grid[i][j]
            to_right[i][n - 1 - j] = to_right[i][n - j] + grid[i][n - 1 - j]
            up[j][i] = up[j - 1][i] + grid[i][j]
            down[n - 1 - j][i] = down[n - j][i] + grid[n - 1 - j][j]
    current_max = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                temp = min(to_left[i][j], to_right[i][j], up[i][j], down[i][j])
                if temp - 1 > current_max:
                    current_max = temp - 1
    if current_max == 0:
        return 0
    else:
        return current_max * 4 + 1


if __name__ == '__main__':

    matrix = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
    ]

    N = 10
    bar = search(matrix)

    # 4 directions of length `4×bar+1` for a middle cell
    print("The largest plus of 1's has a size of", bar)
