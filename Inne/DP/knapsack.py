def knapsack(W, P, max_w):
    n = len(W)
    arr = [[0 for _ in range(max_w + 1)] for _ in range(n)]
    for i in range(W[0], max_w + 1):
        arr[0][i] = P[0]
    for i in range(1, n):
        for w in range(1, max_w + 1):
            arr[i][w] = arr[i - 1][w]
            if w >= W[i]:
                arr[i][w] = max(arr[i][w], arr[i - 1][w - W[i]] + P[i])
    return arr[n - 1][max_w]
