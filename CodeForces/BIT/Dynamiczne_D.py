def pay_least():
    # get input
    n = int(input())
    times_prices = [[0, 0] for _ in range(n)]
    for i in range(n):
        times_prices[i] = [int(x) for x in input().split()]
    tab = [[-1 for _ in range(n)] for _ in range(n)]
    times_prices.sort(key=lambda x: x[1])
    for i in range(min(times_prices[0][0] + 1, n)):
        tab[0][i] = times_prices[0][1]
    end = times_prices[0][0] + 1
    for i in range(1, n):
        end += times_prices[i][0] + 1
        end = min(end, n)
        for j in range(end):
            tab[i][j] = tab[i - 1][j]
            if tab[i][j] == -1:
                if j < times_prices[i][0] + 1:
                    tab[i][j] = times_prices[i][1]
                else:
                    tab[i][j] = tab[i - 1][j - times_prices[i][0] - 1] + times_prices[i][1]
            else:
                if j < times_prices[i][0] + 1 and tab[i][j] > times_prices[i][1]:
                    tab[i][j] = times_prices[i][1]
                elif tab[i - 1][j - times_prices[i][0] - 1] + times_prices[i][1] < tab[i][j]:
                    tab[i][j] = tab[i - 1][j - times_prices[i][0] - 1] + times_prices[i][1]
    smallest = float('inf')
    for i in range(n):
        if tab[i][n - 1] != -1 and tab[i][n - 1] < smallest:
            smallest = tab[i][n - 1]
    print(smallest)


pay_least()
