"""
Dany jest ciag klocków (k1, ..., kn). Klocek ki zaczyna sie na pozycji ai i ciagnie sie do pozycji bi
(wszystkie pozycje to liczby naturalne) oraz ma wysokosc 1. Klocki układane sa po kolei. Jesli
klocek nachodzi na którys z poprzednich, to jest przymocowywany na szczycie poprzedzajacego
klocka. Na przykład dla klocków o pozycjach (1,3), (2,5), (0,3), (8,9), (4,6) powstaje konstrukcja
o wysokosci trzech klocków (vide rysunek). Prosze podac mozliwie jak najszybszy algorytm,
który oblicza wysokosc powstałej konstrukcji (bez implementacji) oraz oszacowac jego złozonosc
obliczeniowa.
Pomysł: Na bazie listy klocków tworzę drzewo przedziałowe.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None


class IntervalTree:
    def __init__(self, intervals):
        pass

