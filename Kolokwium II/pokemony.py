"""
 Student chce wypuścić n różnych pokemonów (numerowanych od 0 don−1) z klatek (poḱeball’i). Wypuszczony Pokemon
 natychmiast atakuje swojego wybawiciela, chyba że (a) jest spokojny, lub (b) w okolicy znajdują się co najmniej
 dwa uwolnione pokemony, na które ten pokemon poluje. Proszę zaimplementować funkcję:
 int* releaseThemAll( HuntingList* list, int n ), gdzie list to lista z informacją, które pokemony polują na które
 (lista nie zawiera powtórzeń):
 struct HuntingList{
    HuntingList* next; // następny element listy
    int predator;      // numer pokemona, który poluje
    int prey;}         // numer pokemona, na którego poluje
Funkcja powinna zwrócić n elementową tablicę z numerami pokemonów w kolejności wypuszczania (tak, żeby wypuszczający
nie został zaatakowany) lub NULL jeśli taka kolejność nie istnieje. Każdy wypuszczony pokemon zostaje ”w okolicy”.
Jeśli pokemon nie występuje na liście jako predator to znaczy, że jest spokojny. Zaimplementowana funkcja powinna
być możliwie jak najszybsza. Proszę krótko oszacować jej złożoność.

Zależności między pokemonami można przedstawić w formie grafu skierowanego, gdzie krawędź z u do v istnieje jeżeli
pokemon u poluje na pokemona v. Wykonuje algorytm DFS, oprócz pola visited dla każdego wierzchołka zapamiętując pole
processed (0/1). Kiedy przetwarzam wierzchołek sprawdzam, czy zachodzi jeden z dwóch warunków:
1) wierzchołek nie ma dzieci
2) wierzchołek ma conajmniej dwoje przetworzonych dzieci
Jeśli nie zachodzi żaden z warunków, to nie istniej właściwa kolejnośc wypuszczania. W przeciwnym wypadku dodaje
pokemona na koniec kolejki wypuszczania.
Złożoność obliczeniowa: O(n + e), gdzie e to sumaryczna liczba ofiar (przy czym e < n^2)
"""


from queue import LifoQueue


# dla uproszczenia, bo nie piszę w C, zakładam że hunting_list to tablicę krotek
def release_them_all(hunting_list, n):
    # create graph
    graph = [[] for _ in range(n)]
    for animal in hunting_list:
        graph[animal[0]].append(animal[1])
    dfs_queue = LifoQueue()
    visited = [False for _ in range(n)]
    processed = [False for _ in range(n)]
    indexes = [0 for _ in range(n)]
    result = []
    for i in range(n):
        if not visited[i]:
            dfs_queue.put(i)
            visited[i] = True
            while not dfs_queue.empty():
                temp = dfs_queue.get()
                while indexes[temp] < len(graph[temp]) and visited[graph[temp][indexes[temp]]]:
                    indexes[temp] += 1
                if indexes[temp] < len(graph[temp]):
                    visited[graph[temp][indexes[temp]]] = True
                    dfs_queue.put(temp)
                    dfs_queue.put(graph[temp][indexes[temp]])
                    indexes[temp] += 1
                else:
                    processed[temp] = True
                    count = 0
                    for child in graph[temp]:
                        if processed[child]:
                            count += 1
                        if count > 1:
                            break
                    if count > 1 or len(graph[temp]) == 0:
                        result.append(temp)
                    else:
                        return None
    return result


test = [(0, 1), (0, 6), (1, 2), (1, 3), (2, 4), (2, 0), (2, 5)]
print(release_them_all(test, 7))
