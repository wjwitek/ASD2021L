def quasibinary():
    n = int(input())
    num = []
    while n > 0:
        num.append(n % 10)
        n //= 10
    num.reverse()
    number_of_bin = max(num)
    print(number_of_bin)
    start = 0
    n = len(num)
    while start < n:
        while num[start] != 0:
            k = start
            while k < n:
                if num[k]:
                    print(1, end="")
                    num[k] -= 1
                else:
                    print(0, end="")
                k += 1
            print(" ", end="")
        while start < n and num[start] == 0:
            start += 1


quasibinary()
