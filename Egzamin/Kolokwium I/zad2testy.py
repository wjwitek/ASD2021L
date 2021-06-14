G1= [[0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 120],
    [-1, 0, 0, 0, 0, 0, 0, 0]]
a1,b1 = 0,7
odp1 = ("Bob",6,[0,1,2,3,4,5,6,7])


G2 = [[0, 1, 0, 0, 0, 15, 0, 0], [0, 0, 5, 0, 0, 0, 0, 0], [0, 0, 0, 0, 7, 0, 110, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 7, 0, 0, 8, 100, 90], [0, 0, 0, 0, 8, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 7, 0]]
a2,b2 = 0,6
odp2 = ("Bob",5,[0,1,2,6])

G3 = [[0, 100, 50], [0, 0, 12], [0, 0, 0]]
a3,b3 = 0,2
odp3 = ("Bob",0,[0,2])

G4 = [[0, 100, 50, 0, 0], [0, 0, 12, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
a4,b4 = 0,4
odp4 = (None,None,None)


test = [(G1,a1,b1,odp1),
        (G2,a2,b2,odp2),
        (G3,a3,b3,odp3),
        (G4,a4,b4,odp4)]

random_wrong = ["https://www.youtube.com/watch?v=AHdfqDWl3T4",
        "https://www.youtube.com/watch?v=VPBbqc8W47Q",
        "https://www.youtube.com/watch?v=gAxVR2tvpA4 dobra ja sie cykam jak to mialo dzialac",
        "https://www.youtube.com/watch?v=1p6Fp2bkw4Y destroyed",
        "https://www.youtube.com/watch?v=-h057K7E3io",
        ]


random_good = ["https://www.youtube.com/watch?v=D_UKuVGzCHk wzz wzz wzz ojciec ma boscha",
        "https://www.youtube.com/watch?v=ytSsGn3E-ic",
        "https://www.youtube.com/watch?v=ZZMxFPNqZLk mozesz isc pic bo dziala",
        "https://www.youtube.com/watch?v=fTFL-hNoQuE ten wieśniacki sweter",
        "https://www.youtube.com/watch?v=8TTU-ivcy6M",
        "https://www.youtube.com/watch?v=3OWSjjcAswM",
        "https://www.youtube.com/watch?v=9Xfv1qzSX5I",
        "https://www.youtube.com/watch?v=XrzqiIhU5cU"]

from random import randint
counter = 1
def runtests(f):
    gites = True
    for G,a,b,odp in test:
        print()
        print("test nr x. Graf wejsciowy:")
        print(*G,sep="\n")
        print("poczatek",a,"koniec",b)
        imie, odlegosc, sciezka = f(G,a,b)
        odp_i, odp_o, odp_s = odp
        if imie != odp_i:
            print("Zła osoba startuje, powinna", odp_i,"a u ciebie staruje",imie)
            gites = False
        if odlegosc != odp_o:
            print("Zła odleglosc tw_wynik",odlegosc,"oczekiwana",odp_o)
            gites = False
        if sciezka != odp_s:
            print("Zla sciezka")
            print("mialo byc:",odp_s)
            print("a tw funkcja zwrocila:",sciezka)
            gites = False
    print()
    if gites:
        print(random_good[randint(0,len(random_good)-1)])
        print("Testy przechodzi")
    else:
        print(random_wrong[randint(0,len(random_wrong)-1)])
        print("Cos jest nie tak")





