"""
Proszę napisać funkcję bool possible( char* u, char* v, char* w ), która zwraca prawdę
jeśli z liter słów u i v da się ułożyć słowo w (nie jest konieczne wykorzystanie wszystkich liter)
oraz fałsz w przeciwnym wypadku. Można założyć, że w i v składają się wyłącznie z małych liter alfabetu
łacińskiego. Proszę krótko uzasadnić wybór zaimplementowanego algorytmu.
"""


def possible(u, v, w):
    alphabet = [0] * 26
    for letter in u:
        alphabet[ord(letter) - ord('a')] += 1
    for letter in v:
        alphabet[ord(letter) - ord('a')] += 1
    for letter in w:
        index = ord(letter) - ord('a')
        if alphabet[index] == 0:
            return False
        else:
            alphabet[index] -= 1
    return True


print(possible("aba", "tet", "l"))
