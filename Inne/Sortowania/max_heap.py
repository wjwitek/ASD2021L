class MaxHeap:
    def __init__(self, idx=0):
        self.length = 0
        self.array = []
        self.idx = idx

    def heapify(self, i):
        l = 2 * i + 1
        r = (i + 1) * 2
        largest = i
        idx = self.idx
        if l < self.length and self.array[i][idx] < self.array[l][idx]:
            largest = l
        if r < self.length and self.array[largest][idx] < self.array[r][idx]:
            largest = r
        if largest != i:
            self.array[largest], self.array[i] = self.array[i], self.array[largest]
            self.heapify(largest)

    def get(self):
        if self.length < 1:
            print("Cannot get value from empty heap")
            exit(1)
        maximum = self.array[0]
        self.array[0], self.array[self.length - 1] = self.array[self.length - 1], self.array[0]
        self.length -= 1
        self.heapify(0)
        return maximum

    def increase_key(self, i, new_key):
        if i >= self.length or self.array[i][0] > new_key:
            print("Incorrect key increment")
            exit(1)
        self.array[i][0] = new_key
        while i > 0 and self.array[(i - 1) // 2][0] < self.array[i][0]:
            self.array[(i - 1) // 2], self.array[i] = self.array[i], self.array[(i - 1) // 2]
            i = (i - 1) // 2

    def put(self, key, additional=None):
        self.length += 1
        self.array.append([0])
        if self.idx == 0:
            temp = [-float('inf')]
        else:
            temp = [-float('inf'), additional]
        self.array[self.length - 1] = temp
        self.increase_key(self.length - 1, key)
