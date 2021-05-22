from zad3testy import runtests

# sortuje liczby od najmniejszej do najwiekszej
# dla kazdej oblicza ile jest jakich cyfr w liczbie
# przechodze i metodą bottom-up uzupelniam tablice dp

# f(i) - najmniejszy koszt aby przejsc z indexyu 0 do i włącznie

# zlozonosc to O(n^2)

def cyfry(a): # obliczam jakie cyfry sa
    c = [0 for _ in range(10)]
    while a != 0:
        c[a%10] += 1
        a//=10
    return c


def find_cost(P):
    n = len(P)
    P.sort() # sortuje liczby

    liczby = [[] for _ in range(n)]
    for i in range(n):
        liczby[i] = cyfry(P[i])

    dp = [float('inf') for _ in range(n)]
    dp[0] = 0 # przejscie z 0 na 0 ma koszt 0

    for i in range(n):
        for j in range(i+1,n):
            for k in range(10):
                if liczby[i][k] > 0 and liczby[j][k] > 0:
                    break
            else: # jezeli nie znalzlem tej samej cyfry
                continue

            dp[j] = min(dp[j],  dp[i] + (abs(P[i]-P[j]))) # jezeli znalzlem ta sama cyfre :

    return -1 if dp[-1] == float('inf') else dp[-1]

runtests(find_cost)
print(find_cost([129, 758, 759, 888]))
