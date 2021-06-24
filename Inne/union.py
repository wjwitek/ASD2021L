class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self

    def find(self):
        if self != self.parent:
            self.parent = self.parent.find()
        return self.parent

    def union(self, other):
        x = self.find()
        y = other.find()
        if x != y:
            if x.rank > y.rank:
                y.parent = x
            else:
                x.parent = y
                if x.rank == y.rank:
                    y.rank += 1
