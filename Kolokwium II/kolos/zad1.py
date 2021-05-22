"""
Weronika Witek
Funkcja rozważa wszystkie nie kolidujące ze sobą budynki o sumarczynej cenie < p, zapamiętując dotychczas obliczone
wyniki i wybiera najlepsze rozwiązanie. Budynki są najpierw ustawiane w graf skierowany, w którym krawędź jest z
wcześniejszego budunku do pożniejszego jeśli ze sobą nie kolidują.
Złożoność czasowa: O(2^n)
Złożoność pamięciowa: O(p*2^n)
"""


from zad1testy import runtests


def select_buildings(T, p):
    n = len(T)
    T = [(T[i][0], T[i][1], T[i][2], T[i][3], i) for i in range(n)]
    T.sort(key=lambda x: x[3])
    # turn into graph
    graph = [[] for _ in range(n)]
    for i in range(n):
        a = T[i][1]
        b = T[i][2]
        for j in range(n):
            if b < T[j][1]:
                graph[i].append(j)
    students = [T[i][0] * (T[i][2] - T[i][1]) for i in range(n)]
    array = [[] for _ in range(p)]
    index = 0
    cheapest = T[0][3]
    while index < n and cheapest:
        array[cheapest].append([index])
        index += 1
    for i in range(cheapest, p):
        for lista in array[i]:
            last = lista[-1]
            for j in graph[last]:
                if i + T[j][3] < p :
                    array[i + T[j][3]].append(lista + [j])
    best_student = 0
    best_price = float('inf')
    result = None
    for i in range(1, p):
        for lista in array[i]:
            suma = 0
            pr = 0
            for building in lista:
                suma += students[building]
            if suma > best_student:
                best_student = suma
                result = lista
                best_price = pr
            elif suma == best_student and pr < best_price:
                best_student = suma
                result = lista
                best_price = pr
    fixed_result = []
    for i in result:
        fixed_result.append(T[i][4])
    fixed_result.sort()
    return fixed_result

runtests( select_buildings )
