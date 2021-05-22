# zadanie obowiązkowe: minimalna liczba tankowań, żeby dotrzeć do t
def min_fill(stations, max_tank):
    # assumes that t is at the end of array stations
    # at each station we fill up to maximum and then go to the furthest station that can be reached
    index = 0
    n = len(stations)
    counter = 0
    while index < n:
        temp = index
        while temp < n - 1 and stations[temp] - stations[index] <= max_tank:
            temp += 1
        if temp == n - 1 and stations[temp] - stations[index] <= max_tank:
            return counter
        index = temp - 1
        counter += 1


"""
min_fill_test_1 = [0, 2, 3, 5, 6, 7, 10, 12, 13, 15, 17, 18]  # max_tank = 4, output = 5
print(min_fill(min_fill_test_1, 4))
"""


# zadanie obowiązkowe: minimalny koszt + tankujemy dowolnie
def min_cost_choice(stations, costs, max_tank):
    # assumes that t is at index n - 1 and start is at index 0 with 0 cost
    current_station = 0
    n = len(stations)
    price = 0
    tank = max_tank
    while True:
        current_lowest = i = current_station + 1
        found_better = False
        while i < n and stations[i] - stations[current_station] <= max_tank:
            if costs[i] <= costs[current_station] and i != n - 1:
                found_better = True
                current_lowest = i
                break
            if costs[i] < costs[current_lowest]:
                current_lowest = i
            if i == n - 1:
                return price + costs[current_station] * (stations[i] - stations[current_station])
            i += 1
        if found_better:
            price += costs[current_station] * (stations[current_lowest] - stations[current_station] - tank)
            tank = 0
            current_station = current_lowest
        else:
            price += costs[current_station] * (max_tank - tank)
            tank = max_tank - (stations[current_lowest] - stations[current_station])
            current_station = current_lowest


"""
test_s = [0, 2, 4, 5, 8, 10, 11, 12, 14, 15, 17, 18, 20, 22]
test_c = [0, 2, 3, 1, 5, 2, 3, 2, 1, 4, 4, 2, 3, 0]
print(min_cost_choice(test_s, test_c, 5))
"""


# zadanie obowiązkowe: minimalny koszt + tankujemy do pełna
def min_cost_full(stations, costs, max_tank):
    # assumes that t is at index n - 1 and start is at index 0 with 0 cost
    n = len(stations)
    partials = [[-1 for _ in range(max_tank)] for _ in range(n)]
    print(partials)
    for i in range(max_tank):
        partials[0][i] = 0
    for i in range(1, n):
        j = i - 1
        while j > -1 and stations[i] - stations[j] <= max_tank:
            k = 0
            temp = max_tank - stations[i] + stations[j]
            while k < max_tank:
                if partials[j][k] == -1:
                    k += 1
                    continue
                if partials[i][temp] == -1 or partials[i][temp] > partials[j][k] + (max_tank - k) * costs[j]:
                    partials[i][temp] = partials[j][k] + (max_tank - k) * costs[j]
                k += 1
            j -= 1
    current_min = partials[n - 1][0]
    print(partials)
    for i in range(1, max_tank):
        if partials[n - 1][i] == -1:
            break
        if partials[n - 1][i] < current_min:
            current_min = partials[n - 1][i]
    return current_min


test_s = [0, 3, 5, 6, 8, 10, 11, 13, 14, 16, 18, 20, 22]
test_c = [0, 2, 1, 3, 5, 4, 2, 1, 3, 5, 4, 7, 0]
print(min_cost_full(test_s, test_c, 4))
