def most_theorem(theorems, awake, k):
    # count number of theories written down without technique
    biggest = 0
    n = len(theorems)
    for i in range(n):
        if awake[i]:
            biggest += theorems[i]
    start = 0
    current = biggest
    while start < n and awake[start] == 1:
        start += 1
    i = 0
    while i < k and start + i < n:
        if not awake[start + i]:
            current += theorems[start + i]
        i += 1
    if current > biggest:
        biggest = current
    while start + k < n:
        if not awake[start]:
            current -= theorems[start]
        if not awake[start + k]:
            current += theorems[start + k]
        start += 1
        if current > biggest:
            biggest = current
    return biggest


def get_most():
    # get input
    n, k = [int(x) for x in input().split()]
    t = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return most_theorem(t, a, k)


print(get_most())
