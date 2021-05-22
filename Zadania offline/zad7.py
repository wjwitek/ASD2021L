"""
Weronika Witek
Kolejka priorytetowa przechowuje "aktywne" węzły w  drzewie tworzonym w celu zakodowania symboli. Bierzemy dwa o
najmniejszej częstości i łączy je w jeden węzeł do kodu mniejszego dodając 0 a do kodu większego dodając 1. 0 i 1 jest
dodawane też do wszystkich węzłów składowych. Pętla kończy się gdy wszystkie symbole są połączone w jeden węzeł.
Złożoność czasowa: O(n^2) - kiedy częstości są takie, że za każdym razem wybierając dwa najmniejsze węzły jednym z nich
jest węzeł złożony z kilku symboli a drugim sam symbol, to taką złożoność ma zarówno samo przypisywanie kodów w pętli
while jak i ich wypisanie później.
"""
from queue import PriorityQueue


S = ["a", "b", "c" ,"d", "e", "f" ]
F = [10 , 11 , 7 , 13, 1 , 20 ]


class Node:
    """
    Class represents a node in a tree constructed when huffman code is constructed
    """
    def __init__(self, l_1=None, l_2=None):
        self.f = 0  # frequency
        self.letter = None  # different than None only for "base" nodes
        self.code = ""  # używam string i konkatenacji, ale można to samo zrobić używając tablicy i trzymając indeks
        # na którym jest ostatni znak, ale tak jest po prostu czytelniej
        self.nodes = [None] * 2
        if l_1 is not None:
            self.nodes[0] = l_1
            self.nodes[1] = l_2
            self.f += l_1.f
            self.f += l_2.f

    def add_code(self, new):
        self.code = new + self.code
        for letter in self.nodes:
            if letter is not None:
                letter.add_code(new)

    # add functions allowing priority queue to compare elements
    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def __gt__(self, other):
        return self.f > other.f

    def __ge__(self, other):
        return self.f >= other.f


def huffman(S, F):
    n = len(S)
    qu = PriorityQueue(n)
    # create array of nodes based on S and F and put them into queue
    symbols = [None] * n
    for i in range(n):
        temp = Node()
        temp.letter = S[i]
        temp.f = F[i]
        symbols[i] = temp
        qu.put(symbols[i])
    while qu.qsize() != 1:
        smaller = qu.get()
        bigger = qu.get()
        smaller.add_code("0")
        bigger.add_code("1")
        temp = Node(smaller, bigger)
        qu.put(temp)
    overall_length = 0
    for i in range(n):
        overall_length += len(symbols[i].code) * symbols[i].f
        print(symbols[i].letter, ":", symbols[i].code)
    print("długość napisu:", overall_length)


huffman(S, F)
