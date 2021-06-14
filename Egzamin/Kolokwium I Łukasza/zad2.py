def swap(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]
    tab[i].set_idx(i)
    tab[j].set_idx(j)

class Element:
    def __init__(self,key : int,value,kopiec):
        self.key = key # priorytet
        self.value = value # wskazanie na Vertex
        self.idx = 0 # index w kopcu
        self.kopiec = kopiec # wskazanie na kopiec

    def __str__(self): # printowanie
        return str(self.key) + " : " + str(self.value)

    def set_idx(self,idx : int): # zmiana indexu w kopcu
        self.idx = idx

    def update_key(self,new_key : int): # zmiana piorytetu
        self.key = new_key
        # self.kopiec.value_changed(self.idx)

    def __lt__(self, other): # do porównywania elementow w kopcu
        return self.key < other.key

class Kopiec:
    def __init__(self):
        self.tab = []
        self.n = 0
    def append(self, elem : Element):
        self.tab.append(elem)
        self.balance_up(self.n)
        self.n += 1

    def pop(self) -> Element:
        ret = self.tab[0]
        swap(self.tab,0,self.n-1)
        self.tab.pop()
        self.n -= 1
        self.balance_down(0)
        return ret

    def __len__(self) -> int:
        return self.n

    def balance_down(self,i : int):
        n = self.n

        mini = i
        left = (2*i)+1
        right = (2*i)+2
        if left < n and self.tab[left] < self.tab[mini]:
            mini = left
        if right < n and self.tab[right] < self.tab[mini]:
            mini = right
        if mini != i:
            swap(self.tab, i, mini)
            self.balance_down(mini)

    def balance_up(self,i):
        if i == 0:
            return
        parent = (i-1)//2
        if self.tab[i] < self.tab[parent]:
            swap(self.tab, i, parent)
            self.balance_up(parent)

    def value_changed(self,i):
        self.balance_up(i)
        self.balance_down(i)

    def __str__(self):
        ret = ""
        for e in self.tab:
            ret += "," + str(e.value.value)+"-"+str(e.key)+","
        return ret

class Vertex:
    def __init__(self, key, kopiec, value,typ):
        self.key = key # priorytet w kopcu
        self.value = value # index albo wskazanie na element zewnetrzny, nie jest potrzebne do kopca
        self.visited = False # nie jest potrzebne do kopca
        self.typ = typ
        self.parent = None

        self.elem = Element(key,self,kopiec) # dodaje do kopca self.elem
        # kopiec.put(self.elem)

    def __str__(self):
        return str(self.value) + " -> " + str(self.key) + "," + str(self.parent)

    def relax(self,new_d): # ustawiam nowy priorytet i zawiadamiam kopiec o tym
        self.key = new_d
        self.elem.update_key(new_d)

def fin_sciezka(first: Vertex, a) -> (Vertex,list):
    last = first
    wynik = []
    while last.value != a:
        wynik.append(last.value)
        last = last.parent
    wynik.append(last.value)
    return last,wynik

bob = 0
alicja = 1
from queue import PriorityQueue
def alicja_und_bob(G, a, b):
    n = len(G)
    big_kopiec = PriorityQueue()
    nowa = [[],[]]
    inf = float('inf')

    for i in range(n):
        nowa[bob].append(Vertex(key = inf, \
                           kopiec = big_kopiec, \
                           value = i,\
                           typ= bob))
        nowa[alicja].append(Vertex(key=inf,\
                        kopiec=big_kopiec,\
                        value=i,\
                        typ=alicja))

    nowa[bob][a].relax(0)
    nowa[alicja][a].relax(0)
    big_kopiec.put(nowa[bob][a].elem)
    big_kopiec.put(nowa[alicja][a].elem)

    while big_kopiec.qsize() != 0:
        elem = big_kopiec.get()
        if elem.value.typ == bob:
            # tu teraz bedzie alicja (placimy)
            for i in range(len(G)):
                if G[elem.value.value][i] > 0:
                    idx_sasiada = i
                    waga = G[elem.value.value][i]

                    sasiad = nowa[alicja][idx_sasiada] # typ - Vertex
                    if sasiad.key > elem.key + waga:
                        sasiad.relax(elem.key+waga)
                        big_kopiec.put(sasiad.elem)
                        sasiad.parent = elem.value

        elif elem.value.typ == alicja:
            # tu bob (nie placimy)
            for i in range(len(G)):
                if G[elem.value.value][i] > 0:
                    idx_sasiada = i

                    sasiad = nowa[bob][idx_sasiada] # typ - Vertex
                    if sasiad.key > elem.key:
                        sasiad.relax(elem.key)
                        big_kopiec.put(sasiad.elem)
                        sasiad.parent = elem.value


    if nowa[bob][b].key == float('inf') and nowa[alicja][b].key == float('inf'):
        return None,None,None
    ret_imie = None
    if nowa[bob][b].key < nowa[alicja][b].key:
        last, sciezka = fin_sciezka(nowa[bob][b], a)
        if last.typ == alicja:
            ret_imie = "Bob"
        else:
            ret_imie = "Alicja"
    else:
        last, sciezka = fin_sciezka(nowa[alicja][b], a)
        if last.typ == alicja:
            ret_imie = "Bob"
        else:
            ret_imie = "Alicja"

    return ret_imie,min(nowa[bob][b].key,nowa[alicja][b].key),sciezka[::-1]




if __name__ == "__main__":
    from zad2testy import runtests
    runtests(alicja_und_bob)
