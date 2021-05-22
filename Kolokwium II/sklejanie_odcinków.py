"""
Dany jest ciąg przedziałów postaci [ai, bi]. Dwa przedziały można skleić jeśli mają dokładnie jeden punkt wspólny.
Proszę wskazać algorytmy dla następujących problemów:
1. Problem stwierdzenia, czy da się uzyskąć przedział [a, b]przez sklejanie odcinków.
2. Zadanie jak wyżej, ale każdy odcinek ma koszt i pytamy o minimalny koszt uzyskania odcinka[a, b].
3. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków.
Założenie: wszystkie przedziały zawierają się w [a, b]
Problem 1: f(i) - czy można uzyskać odcinek kończący się w bi
Problem 2: f(i) - najtańszy koszt uzyskania odcinka kończącego się w bi
Problem 3: f(i, j) - minimalna liczba przedziałów potrzebna do utworzenia odcinka zaczynającego się w ai i kończącego w
bi (bez implementacji)
"""


def can_be_created(parts, a, b):
    sorted(parts, key=lambda x: x[0])
    n = len(parts)
    possible = [False for _ in range(n)]
    if parts[0][0] == a:
        possible[0] = True
    else:
        return False
    for i in range(1, n):
        for j in range(i):
            if (parts[i][0] == parts[j][1] and possible[j]) or parts[i][0] == a:
                possible[i] = True
                break
    i = n - 1
    print(possible)
    while i > -1 and parts[i][1] == b:
        if possible[i]:
            return True
        i -= 1
    return False


"""
test = [(1, 2), (1, 3), (3, 4), (4, 5), (4, 6)]
print(can_be_created(test, 1, 7))
"""


def cheapest(parts, a, b, costs):
    sorted(parts, key=lambda x: x[0])
    n = len(parts)
    possible = [float('inf') for _ in range(n)]
    if parts[0][0] == a:
        possible[0] = costs[0]
    else:
        return float('inf')
    for i in range(1, n):
        for j in range(i):
            if (parts[i][0] == parts[j][1] and possible[j]) or parts[i][0] == a:
                if possible[i] > possible[j] + costs[i]:
                    possible[i] = possible[j] + costs[i]
    i = n - 1
    minimum = float('inf')
    while i > -1 and parts[i][1] == b:
        if possible[i] < minimum:
            minimum = possible[i]
        i -= 1
    return minimum


test = [(1, 2), (1, 3), (3, 4), (2, 5), (4, 7), (5, 7)]
test_costs = [3, 4, 1, 5, 2, 0]
print(cheapest(test, 1, 7, test_costs))



