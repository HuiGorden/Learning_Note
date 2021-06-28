#!python3

class disjointSet:

    def __init__(self, n):
        # For recoding parent
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            rootNode = self.find(self.parent[x])
            self.parent[x] = rootNode
        return self.parent[x]

    def merge(self, x, y):
        rootNodeX = self.find(x)
        rootNodeY = self.find(y)
        if rootNodeX == rootNodeY:
            return
        if self.rank[rootNodeX] < self.rank[rootNodeY]:
            self.parent[rootNodeX] = rootNodeY
        elif self.rank[rootNodeX] > self.rank[rootNodeY]:
            self.parent[rootNodeY] = rootNodeX
        else:
            self.parent[rootNodeX] = rootNodeY
            self.rank[rootNodeX] += 1


testDisjointSet = disjointSet(5)
testDisjointSet.merge(0, 2)
testDisjointSet.merge(4, 2)
print(f"Is element 4 and element 0 in same set? {testDisjointSet.find(4) == testDisjointSet.find(0)}")
print(f"Is element 1 and element 0 in same set? {testDisjointSet.find(1) == testDisjointSet.find(0)}")

