"""
Zbiór przedziałów {[a1, b1], ...,[an, bn]}, każdy przedział należy do [0,1]. Opisać algorytm który sprawdzi czy jest
możliwy taki wybór przedziałów, aby cały przedział [0,1] zawierał się w wybranych odcinkach. Przedział ma składać się z
jak najmniejszej ilości odcinków.
"""


from random import shuffle


def find_sets(sets):
    sets.sort(key=lambda x: x[1], reverse=True)
    sets.sort(key=lambda x: x[0])
    n = len(sets)
    counter = 1
    if sets[0][0] != 0:
        return -1
    index = 0
    b = sets[0][1]
    while True:
        temp = index
        while temp < n and sets[temp][0] <= b:
            temp += 1
        temp -= 1
        if temp == index or (temp == n - 1 and sets[temp][1] != 1):
            return -1
        index = temp
        b = sets[index][1]
        counter += 1
        if b == 1:
            return counter


test = [(0, 0.5), (0.6, 1), (0.3, 0.7)]
shuffle(test)
print(find_sets(test))
