"""
Dany jest ciąg klocków (k1, ..., kn). Klocek ki zaczyna się na pozycji ai i ciągnie się do pozycji bi (wszystkie pozycje
to liczby naturalne) oraz ma wysokość 1. Klocki układane są po kolei. Jeśli klocek nachodzi na któryś z poprzednich, to
jest przymocowywany na szczycie poprzedzającego klocka. Na przykład dla klocków o pozycjach (1,3), (2,5), (0,3), (8,9),
(4,6) powstaje konstrukcjao wysokości trzech klocków (vide rysunek). Proszę podać możliwie jak najszybszy algorytm,
który oblicza wysokość powstałej konstrukcji (bez implementacji) oraz oszacować jego złożoność obliczeniową.
Założenie: wysokość konstrukcji oznacza najwyższy punkt konstrukcji, tj, pod najwyższym punktem konstukcji może
znajdować się pusta przerwa.
Złożoność obliczeniowa: O(n * m + u), gdzie m to długość największego klocka, a u to rónica między największym bi a
najmniejszym ai
"""


def tower(blocks):
    # find min ai and max bi
    n = len(blocks)
    min_a, max_b = float('inf'), 0
    for i in range(n):
        if blocks[i][0] < min_a:
            min_a = blocks[i][0]
        if blocks[i][1] > max_b:
            max_b = blocks[i][1]
    table = [0 for _ in range(max_b - min_a)]
    for i in range(n):
        for j in range(blocks[i][0] - min_a, blocks[i][1] - min_a):
            table[j] += 1
    # find highest point on table
    maximum = 0
    for i in range(len(table)):
        if table[i] > maximum:
            maximum = table[i]
    return maximum


test = [(1, 3), (2, 5), (0, 3), (8, 9), (4, 6)]
print(tower(test))
