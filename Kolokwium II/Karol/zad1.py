def easy_path(T):
    
    # chyba nie działa, gdybym dodał, że DFS wywołuje dla początów ścieżki byłoby chyba ok
    class Graph():

        class Vertex():

            def __init__(self, idx, adj = [], color = 0):
                self.idx = idx
                self.adj = adj
                self.color = color
                self.st = len(self.adj)
            
            def __index__(self):
                return self.idx
            
            def __str__(self):
                return f'Node {self.idx}'

        def __init__(self, adjList):
            self.vertices = [None]*len(adjList)
            for i in range(len(self.vertices)):
                self.vertices[i] = self.Vertex(i, adjList[i])

    def DFS(G):

        def DFS_Visit(G,u):
            nonlocal x
            nonlocal maxi
            u.color = 1
            for v in u.adj:
                v = G.vertices[v]
                if v.color == 0 and v.st <= 2:
                    x += 1
                    DFS_Visit(G, v)
            u.color = 1
            maxi = max(x, maxi)
            x -= 1
        
        maxi = float('-inf')
        x = 0
        for u in G.vertices:
            if u.color == 0 and u.st <= 2:
                DFS_Visit(G, u)
                x = 0
        return maxi
    
    G = Graph(T)
    return DFS(G)



T1 = [[1], [2, 0, 8, 4], [3, 1], [2], [1], [6], [7, 5], [6, 8], [1, 7]]
print("Git" if easy_path(T1) == 3 else "chuj nie dziala") # 3


T2 = [[1], [2, 0, 9, 12, 13], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6, 12, 13], [9, 7], [10, 8, 1, 12], [11, 9], [10], [7, 9, 1], [1, 7]]
print("Git" if easy_path(T2) == 4 else "chuj nie dziala") # 4

T3 = [[2, 7], [2, 6], [0, 1], [6], [4], [5], [3, 4, 5, 1], [8, 9, 10], [7], [7], [7]]
print("Git" if easy_path(T2) == 2 else "chuj nie dziala") # 2
