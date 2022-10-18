class Graph:
     
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def applyUnion(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.applyUnion(parent, rank, x, y)
        for u, v, weight in result:
            print("Vertice:",u, v,end =" ")
            print("-",weight)
 

# Grafo 1
print("Grafo 1")
g = Graph(8)
g.addEdge(0, 3, 9)
g.addEdge(0, 7, 3)
g.addEdge(0, 4, 4)
g.addEdge(1, 3, 10)
g.addEdge(1, 2, 1)
g.addEdge(2, 3, 6)
g.addEdge(3, 4, 3)
g.addEdge(4, 5, 2)
g.addEdge(4, 7, 7)
g.addEdge(5, 6, 5)
g.addEdge(5, 7, 14)
g.addEdge(6, 7, 4)
g.kruskal()


print("Grafo 2")
g = Graph(14)
g.addEdge(0, 4, 1)
g.addEdge(0, 5, 4)
g.addEdge(0, 11, 5)
g.addEdge(1, 4, 2)
g.addEdge(1, 8, 7)
g.addEdge(1, 2, 8)
g.addEdge(2, 3, 3)
g.addEdge(2, 5, 4)
g.addEdge(2, 6, 1)
g.addEdge(2, 9, 2)
g.addEdge(3, 6, 2)
g.addEdge(3, 13, 5)
g.addEdge(4, 7, 8)
g.addEdge(5, 6, 4)
g.addEdge(5, 8, 1)
g.addEdge(5, 12, 3)
g.addEdge(7, 8, 8)
g.addEdge(9, 10, 10)
g.addEdge(9, 11, 5)
g.addEdge(9, 12, 8)
g.addEdge(10, 13, 7)
g.kruskal()