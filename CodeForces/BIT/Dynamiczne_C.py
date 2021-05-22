def spreadsheet():
    # get table
    n, m = [int(x) for x in input().split()]
    tab = []
    for i in range(n):
        tab.append([int(x) for x in input().split()])
    possible = [i for i in range(n)]
    k = int(input())
    problems = [[int(x) - 1 for x in input().split()] for _ in range(k)]
    minimum = problems[0][0]
    for i in range(k):
        if minimum > problems[i][0]:
            minimum = problems[i][0]
    maximum = problems[0][1]
    for i in range(k):
        if maximum < problems[i][1]:
            maximum = problems[i][1]
    for j in range(m):
        start = minimum
        while start < maximum:
            end = start + 1
            while end < maximum + 1 and tab[end - 1][j] <= tab[end][j]:
                end += 1
            for i in range(start, end):
                if end - 1 > possible[i]:
                    possible[i] = end - 1
            start = end

    # solve tasks
    for i in range(k):
        l, r = problems[i]
        if r <= possible[l]:
            print("Yes")
        else:
            print("No")


spreadsheet()
