class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


def add_nodes(node, p, r, points):
    mid = (r - p) // 2


class Tree:
    def __init__(self, array):
        points = []
        for a, b in array:
            if a not in points:
                points.append(a)
            if b not in points:
                points.append(b)
        points.sort()

        p, r = 0, len(points) - 1
        while True:
            mid = (r - p) // 2
