""" Algorytm na początek za pomocą funkcji select wyszukuje obecne indeksy elementów które w posortowanej tablicy znajdowały by się
na indeksach p i q, następnie wykonuje dwa przejścia quicksorta by między p i q trafiły wszystkie potrzebne elementy i wykonujemy już
pełnego quicksorta na tym właśnie przedziale """


def hoare(A, p, r,pivot):           #jak coś to w quicksorcie i selectie dałem jako czwarty argument początek, bo zwykle w funkcji hoare jako pivot
    x = A[pivot]                    # się przyjmuje A[poczatek] a było potrzebne żeby potem dać tu indeksy curr_p i curr_q
    i = p
    j = r
    while True:
        while A[j] < x:
            j -= 1
        while A[i] > x:
            i += 1
        if i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        else:
            return j


def select(A,p,r,k):
    if p == r: return p
    q = hoare(A,p,r,p)
    if q == k : return q
    elif k < q : return select(A,p,q-1,k)
    else : return select(A,q+1,r,k)


def quicksort(A,p,r):
    if p < r :
        q = hoare(A,p,r,p)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)


def section(T,p,q):
    n = len(T)
    curr_p = select(T,0,n-1,p)              #znalezienie obecnego indeksu p
    curr_q = select(T,0,n-1,q)              #znalezienie obecnego indeksu q
    sorted_p = hoare(T,0,n-1,curr_p)    # te dwie linijki są zbędne - select już sam takie sortowanie
    sorted_q = hoare(T,sorted_p,n-1,curr_q)        #ograniczenie quicksorta do przedzialu p - q
    quicksort(T,p,q)                           #sortujemy przedział (bo chyba trzeba, nie ma sprecyzowanego w zadaniu czy lista pomiędzy ma być posortowana)
    return T[p:q+1]                              # ale chuj, nawyżej quicksort do wyjebania
    # drobna zmiana - slicing jest prawostronnie otwarty a w poleceniu jest włącznie

T = [10,15,34,80,97,15,24,34,11,8,2,3]
print(section(T,5,8))
print(sorted(T))
