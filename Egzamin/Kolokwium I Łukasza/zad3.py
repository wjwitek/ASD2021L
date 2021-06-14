def znajdz_sciezke(G, lasty, X,Y, sciezka):
    if X == Y:
        return sciezka
    while lasty[X] >= 0:
        lasty[X]-=1
        a = znajdz_sciezke(G,lasty,G[X][lasty[X]+1],Y,sciezka + [X])
        if a != None:
            return a
    return None

def dfs(G, lasty, X,Y, parent,wchodzace,visited_2):
    visited_2[X] = True
    while lasty[X] >= 0:
        lasty[X]-=1

        parent[G[X][lasty[X]+1]].append(X)
        wchodzace[G[X][lasty[X]+1]] += 1
        dfs(G,lasty,G[X][lasty[X]+1],Y,parent,wchodzace,visited_2)

def dfs_2(G, X,Y,visited, sciezka, poprz_sciezka, idx,ez = True):
    visited[X] = teraz_ogarniety
    for i in G[X]:
        if nieodwiedzony == visited[i]:
            visited[i] = teraz_ogarniety
            sciezka.append(i)
            dfs_2(G,i,Y,visited,sciezka,poprz_sciezka,idx,False)
            if ez:
                sciezka.append(X)

    if idx >= len(poprz_sciezka):
        return sciezka

    if ez:
        sciezka.append(poprz_sciezka[idx])
        dfs_2(G,poprz_sciezka[idx],Y,visited,sciezka,poprz_sciezka,idx+1,True)

    return sciezka


# o kurwa nie wiem nawet jak to wytlumaczyc, zlonosc jest O(V+E)
# lece raz dfsem znajduje jakkolwiek dojscie do Y i sprawdzam czy sie da wgl zrobic tka sciezke zeby dzialalo (wchodzace i wychodzace sciezki musa sie zgadzac)
# pozniej tworze przykladowa sciezke z częścią cykli jezeli sie napatocza
# ponziej na podstawie tej sciezki tworze sciezke faktyczna tak ze sprawdzam czy jest jakas krawedz wychodzaca ktora nie jest w przykladowej sciezce
# wtedy ide w ten cykl, i na powrocie dodaje jeszcze raz wierzcholek ktory spaja sciezke i cykl
# jezeli przejde przez wszystkie cykle ktore przechodza tą ścieżką
# to ide dalej po przykaldowej sciezce
w_sciezce = 1
nieodwiedzony = 0
teraz_ogarniety = 2
def darmowe_przejazdy_XD(T,X,Y):
    # T[0] = (a,b) - skad i dokad jedzie ten busik

    # to byl zart z ta lista krawedzi odrazu na liste saisedzztw robie
    maxi = 0
    for a,b in T:
        maxi = max(maxi,a,b)

    # maxi+1 jest wierzcholkow
    sasiady = [[] for _ in range(maxi+1)]

    for a,b in T:
        sasiady[a].append(b)

    lasty = [len(sasiady[i])-1 for i in range(maxi+1)]
    parenty = [[] for _ in range(maxi+1)]
    wchodzace = [0 for _ in range(maxi+1)]
    visited_2 = [False for _ in range(maxi+1)]
    dfs(sasiady,lasty,X,Y,parenty, wchodzace,visited_2)

    for i in range(maxi+1):
        if i == Y:
            if wchodzace[i] -1 != len(sasiady[i]):
                return False
        elif i == X:
            if wchodzace[i] != len(sasiady[i])-1:
                return False
        else:
            if wchodzace[i] != len(sasiady[i]):
                return False

    lasty = [len(sasiady[i])-1 for i in range(maxi+1)]
    visited = [nieodwiedzony for i in range(maxi+1)]

    sciezka = znajdz_sciezke(sasiady,lasty,X,Y,[])

    if sciezka == None:
        return False
    sciezka.append(Y)

    # wiemy ze sie da przejsc ale pytanie czy w przykaldowej sciezce 
    # sa wszystkie wierzcholki do ktorych krawedzie
    for i in range(maxi+1):
        if not visited_2[i]:
            visited[i] = teraz_ogarniety # tutaj wierzcholki ktore wgl nei sa spojne

    for i in range(len(sciezka)):
        visited[sciezka[i]] = w_sciezce
    for i in range(maxi+1):
        if visited[i] == nieodwiedzony:
            break
    else:
        return sciezka

    sciezka_2 = dfs_2(sasiady,X,Y,visited,[],sciezka,0)
    return sciezka_2


if __name__ == "__main__":
    from zad3testy import runtests
    runtests(darmowe_przejazdy_XD)
G6 = [(1, 2), (1, 0), (2, 5), (2, 3), (3, 7), (3, 4), (0, 2), (0, 5), (0, 6), (5, 8), (5, 3), (5, 7), (6, 5),
      (7, 0), (7, 1), (8, 0)]
a6, b6 = 1, 4
odp6 = [1, 0, 2, 5, 7, 0, 5, 0, 6, 5, 3, 7, 1, 2, 3, 4]  # przy czym jest to odp przykładowa, jest kilka możliwości

G7 = [(0, 1), (0, 3), (1, 2), (1, 5), (5, 6), (6, 3), (3, 1), (3, 4), (4, 0)]
a7, b7 = 0, 2
odp7 = [0, 3, 4, 0, 5, 6, 0, 1, 2]

G8 = [(0, 1), (1, 2), (2, 3), (3, 2), (3, 4), (2, 5), (5, 3)]
a8, b8 = 0, 4
odp8 = [0, 1, 2, 3, 2, 5, 3, 4]

print(darmowe_przejazdy_XD(G6, 1, 4))
print(darmowe_przejazdy_XD(G7, a7, b7))
print(darmowe_przejazdy_XD(G8, a8, b8))
