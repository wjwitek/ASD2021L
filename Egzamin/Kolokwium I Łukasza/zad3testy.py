G1 = [(0,1),(1,2),(2,3)]
a1,b1 = 0,3
odp1 = [0,1,2,3]

G2 = [(0,1),(1,2),(2,3),(1,3)]
a2,b2 = 0,3
odp2 = False

G3 = [(0, 1),(1, 2),(2, 3),(3,1),(1,4),(4,5)]
a3,b3 = 0,5
odp3 = [0,1,2,3,1,4,5]

G4 = [(0, 1),(1, 2),(2, 3),(4, 5),(5, 0),(0, 4)]
a4,b4 = 0,3
odp4 = [0,4,5,0,1,2,3]

G5 = [(0, 1),(1, 2),(2, 3),(4, 5),(5, 0),(0, 4),(5,6),(6,7),(7,8),(8,5)]
a5,b5 = 0,3
odp5 = [0,4,5,6,7,8,5,0,1,2,3]


test = [(G1,a1,b1,odp1),(G2,a2,b2,odp2),(G3,a3,b3,odp3),(G4,a4,b4,odp4),(G5,a5,b5,odp5)]

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
def runtests(f):
    gites = True
    for G,a,b,odp in test:
        print()
        print("Krawedzie wejsciowe")
        print(G)
        print("poczatek",a,"koniec",b)
        wynik = f(G,a,b)
        if odp != wynik:
            print("Zla sciezka")
            print("mialo byc:",odp)
            print("a tw funkcja zwrocila:",wynik)
            gites = False
    print()
    if gites:
        print(random_good[randint(0,len(random_good)-1)])
        print("Testy przechodzi")
    else:
        print(random_wrong[randint(0,len(random_wrong)-1)])
        print("Cos jest nie tak")





