def print_subsequences(array, end_row, end_col):
    biggest = -1
    counter = 0
    for i in range(end_col + 1):
        if array[end_row][i] != -1:
            counter += 1
            if array[end_row][i] > biggest:
                biggest = array[end_row][i]
    for i in range(end_row - 1, -1, -1):
        new_biggest = -1
        partial_counter = 0
        for j in range(end_col - (end_row - i) + 1):
            if array[i][j] == -1:
                continue
            partial_counter += 1
            if array[i][j] >= biggest:
                array[i][j] = -1
                partial_counter -= 1
            elif array[i][j] > new_biggest:
                new_biggest = array[i][j]
        biggest = new_biggest
        counter *= partial_counter
    # counter represents maximum number of subsequences based on remaining numbers for each position
    sequences = [[-1] * (end_row + 1) for _ in range(counter)]
    free_row = 0
    for i in range(end_col - end_row + 1):
        if array[0][i] == -1:
            continue
        sequences[free_row][0] = array[0][i]
        free_row += 1
    for i in range(1, end_row + 1):
        biggest_in_row = True
        free_row_temp = free_row
        for j in range(end_col - (end_row - i) + 1):
            if array[i][j] == -1:
                continue
            if biggest_in_row:
                for k in range(free_row):
                    sequences[k][i] = array[i][j]
                biggest_in_row = False
            else:
                for k in range(free_row):
                    if sequences[k][i - 1] < array[i][j]:
                        for l in range(i):
                            sequences[free_row_temp][l] = sequences[k][l]
                        sequences[free_row_temp][i] = array[i][j]
                        free_row_temp += 1
            free_row = free_row_temp
    count_sequences = 0
    for row in sequences:
        if row[end_row] != -1:
            for i in row:
                print(i, end=" ")
            print()
            count_sequences += 1
    return count_sequences


def find_index(smallest, end_row, new_value):
    p, r = 0, end_row
    while r - p > 1:
        mid = p + (r - p) // 2
        if smallest[mid] >= new_value:
            r = mid
        else:
            p = mid
    return r


def find_subsequences(array):
    n = len(array)
    grid = [[-1] * n for _ in range(n)]
    smallest = [-1] * n
    biggest = [-1] * n
    indexes = [0] * n
    grid[0][0] = array[0]
    smallest[0] = array[0]
    biggest[0] = array[0]
    indexes[0] = 1
    end_row = end_col = 0
    end_col_row = 0
    for i in range(1, n):
        value = array[i]
        if value > biggest[end_row]:
            grid[end_row + 1][end_col] = value
            end_row += 1
            biggest[end_row] = value
            smallest[end_row] = value
            indexes[end_row] = end_col + 1
        elif value < smallest[0]:
            grid[0][end_col] = value
            smallest[0] = value
            indexes[0] = end_col + 1
        else:
            row = find_index(smallest, end_row, value)
            if end_col_row > row:
                end_col += 1
                end_col_row = row
            if end_col < indexes[row]:
                end_col = indexes[row]
                end_col_row = row
            grid[row][end_col] = value
            smallest[row] = value
            indexes[row] = end_col + 1
    print_subsequences(grid, end_row, end_col)
