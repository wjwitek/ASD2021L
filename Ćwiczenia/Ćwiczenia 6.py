"""
Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Lasskłada się zndrzew rosnących na pozycjach
0, . . . , n−1. Dla każdegoi∈{0, . . . , n−1}znany jest zyskci, jakimożna osiągnąć ścinając drzewo z pozycjii.
John Lovenoses chce uzyskać maksymalny zysk ze ścinanychdrzew, ale prawo zabrania ścinania dwóch drzew pod rząd.
Proszę zaproponować algorytm, dzięki któremuJohn znajdzie optymalny plan wycinki.
"""


def f(i):
    global V
    if i in memoF:
        return memoF[i]
    if i == 0:
        memoF[i] = V[0]
        return memoF[i]
    memoF[i] = g(i-1) + V[i]
    return memoF[i]


def g(i):
    global V
    if i in memoG:
        return memoG[i]
    if i == 0:
        memoG[i] = 0
        return memoG[i]
    memoG[i] = max(f(i-1), g(i-1))
    return memoG[i]


V = [2,3,5,7,1,11,13,0,0,17] * 3
cnt = 0
memoG = {}
memoF = {}


"""
Każdy klocek to przedział postaci[a, b]. Dany jest ciąg klocków[a1, b1],[a2, b2],. . .,[an, bn]. Klocki spadają na oś 
liczbową w kolejności podanej w ciągu. Proszę zaproponowaćalgorytm, który oblicza ile klocków należy usunąć z listy tak, 
zeby każdy kolejny spadajacy klocek mieściłsię w całości w tam, który spadł tuż przed nim.
"""


def blocks(array):
    n = len(array)
    solutions = [1] * n
    for i in range(1, n):
        for j in range(i):
            if array[i][0] >= array[j][0] and array[i][1] <= array[j][1]:
                solutions[i] = max(solutions[i], solutions[j] + 1)
    print(solutions)

