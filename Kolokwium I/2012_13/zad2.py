"""
Proszę zaprojektować strukturę danych przechowującą liczby i pozwalającą na następujące operacje (zakładamy,
że wszystkie liczby umieszczane w strukturze są różne):
Init(n). Tworzy zadaną strukturę danych zdolną pomieścić maksymalnie n liczb.
Insert(x). Dodaje do struktury liczbę x.
RemoveMin(). Znajduje najmniejszą liczbę w strukturze, usuwa ją i zwraca jej wartość.
RemoveMax(). Znajduje największą liczbę w strukturze, usuwa ją i zwraca jej wartość.
Każda z operacji powinna mieć złożoność O(log(n), gdzie n to ilość liczb znajdujących się obecnie w strukturze.
W tym zadaniu nie trzeba implementować podanych operacji, a jedynie przekonująco opisać jak powinny być zrealizowane
i dlaczego mają wymaganą złożoność.
"""


def parent(i): return (i - 1) // 2
def left(i): return 2 * i + 1
def right(i): return 2 * (i + 1)


class MinMaxHeap:
    def __init__(self, n):
        self.free_index = 0
        self.min_heap = [[-1, -1]] * n
        self.max_heap = [[-1, -1]] * n

    def max_repair(self, k=None):
        if k is None:
            k = self.free_index - 1
        while k > 0 and self.max_heap[parent(k)][0] < self.max_heap[k][0]:
            # replace indexes in min heap
            self.min_heap[self.max_heap[parent(k)][1]][1], self.min_heap[self.max_heap[k][1]][1] = k, parent(k)
            # replace rows in max heap
            self.max_heap[parent(k)], self.max_heap[k] = self.max_heap[k], self.max_heap[parent(k)]
            k = parent(k)

    def min_repair(self, k=None):
        if k is None:
            k = self.free_index - 1
        while k > 0 and self.min_heap[parent(k)][0] > self.min_heap[k][0]:
            # replace indexes in max heap
            self.max_heap[self.min_heap[parent(k)][1]][1], self.max_heap[self.min_heap[k][1]][1] = k, parent(k)
            # replace rows in min heap
            self.min_heap[parent(k)], self.min_heap[k] = self.min_heap[k], self.min_heap[parent(k)]
            k = parent(k)

    def insert(self, key):
        if self.free_index == len(self.max_heap):
            print("Array overflow")
            exit(1)
        else:
            self.max_heap[self.free_index] = [key, self.free_index]
            self.min_heap[self.free_index] = [key, self.free_index]
            self.free_index += 1
            self.max_repair()
            self.min_repair()

    def remove_min(self):
        pass
        # swap min with last element, take out min keeping its index from max, than heapify, than swap this num in max
        # with last element throw away last and repair from k


test_heap = MinMaxHeap(7)
test_heap.free_index = 3
test_heap.min_heap = [[2, 2], [4, 4], [5, 0], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
test_heap.max_heap = [[5, 2], [4, 1], [2, 0], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
test_heap.insert(3)
test_heap.insert(7)
test_heap.insert(1)
print(test_heap.min_heap)
print(test_heap.max_heap)
