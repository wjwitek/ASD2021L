from zad3testy import runtests

def find_cost(P):
    # f(i,j) - całkowity koszt dotarcia na i zaczynając z j
    # f(i,j) = min po k (f(i,k) + d(j, k))
    # f(i,i) = 0

    # zlożoność O(n^3) (chyba)

    def dis(i, j, P):
        if can_it(i, j, P):
            return abs(P[i]-P[j])
        else:
            return float('inf')

    def can_it(i, j, P):
        num1 = P[i]
        num2 = P[j]
        while (num1 != 0):
            x = num1 % 10
            num1 //= 10
            cp = num2
            while(cp != 0):
                if (cp % 10 == x):
                    return True
                cp //= 10
        return False

    def find_idx(P):
        n = len(P)
        inf = float('inf')
        
        mini = inf
        mini_idx = -1
        maxi = inf*(-1)
        maxi_idx = -1
        for i in range(n):
            if P[i] < mini:
                mini = P[i]
                mini_idx = i
            if P[i] > maxi:
                maxi = P[i]
                maxi_idx = i
        return(mini_idx, maxi_idx)

    def go_to_parent(parent, k):
        for i in parent:
            if k == i:
                return False
        return True

    def F(P, A, i, j, parent):
        n = len(P)
        if A[i][j] != inf:
            return A[i][j]
        if i == j:
            return 0
        for k in range(n):
            if k != j and go_to_parent(parent, k) and can_it(k, j, P):
                A[i][j] = min(A[i][j], F(P, A, i, k, parent + [j])+dis(j, k, P))
        return A[i][j]
    
    inf = float('inf')
    n = len(P)
    A = [[inf for _ in range(n)] for _ in range(n)]
    j, i = find_idx(P)
    print(A)
    res = F(P, A, i, j, [-1])
    if res == inf:
        return -1
    else:
        return res

#runtests(find_cost)
#print(find_cost([129, 758, 759, 888]))
print(find_cost([1, 12, 23, 30, 35, 55]))
