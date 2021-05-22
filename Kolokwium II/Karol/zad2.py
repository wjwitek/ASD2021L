from zad2testy import runtests

def let( ch ): return ord(ch) - ord("a")

# nie działa :(

def letters( G, W ):
    # sposób mam taki że leci DFS
    # tak że przechodzi do wierzchołka tylko wtedy gdy następna
    # się zgadza. Po drodze sumuje wagi. Dochodze do końca
    # i ustawiam sobie minimum jako obecną sumę wag,
    # cofam się do poprzedniego wierzchołka, odejmując wagę
    # i szukam nie odwiedzonej następnej dobrej litery,
    # zapisuje najelpsze wagi dla każdej przedostatniej litery
    # i powtarzam algortym aż do pierwszej, następnie porownuje wszystkie pierwsze litery
    L , E = G[0], G[1]
    n = len(G[0])
    V = [False for _ in range(n)]
    Res = [0 for _ in range(n)]

    def DFS_visit(L, E, V, u, l, suma):
        nonlocal W
        nonlocal mini
        V[u] = True
        for i in E:
            if i[0] == u and V[i[1]] == False:
                if L[i[1]] == W[l]:
                    suma += i[2]
                    DFS_visit(L, E, V, i[1], l+1, suma)
        if L[u] == W[l-1]:
            mini = min(mini, suma)
        else:
            return -1
        suma -= i[2]

    mini = float('inf')
    for u in range(n):
        if L[u] == W[0] and V[u] == False:
            DFS_visit(L, E, V, u, 1, 0)
    return mini
    

runtests( letters )
    
    
