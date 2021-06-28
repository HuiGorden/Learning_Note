#!python3


class KrusKaAlogrithm:
    def __init__(self):
        self.ajacentMatrix = [
            [0, 1, 3, float("inf"), float("inf")],
            [1, 0, 3, 6, float("inf")],
            [3, 3, 0, 4, 2],
            [float("inf"), 6, 4, 0, 5],
            [float("inf"), float("inf"), 2, 5, 0]
        ]
        self.nodes = [eachNode for eachNode in range(len(self.ajacentMatrix))]
        self.parent = [eachNode for eachNode in range(len(self.ajacentMatrix))]
        self.rank = [1 for eachNode in range(len(self.ajacentMatrix))]
        self.edges = []
        for startNodeIndex in range(len(self.ajacentMatrix)):
            endNodesList = self.ajacentMatrix[startNodeIndex]
            for endNodeIndex in range(len(endNodesList)):
                if startNodeIndex != endNodeIndex and startNodeIndex < endNodeIndex:
                    edgeDict = {
                        "startNodeIndex": startNodeIndex,
                        "endNodeIndex": endNodeIndex,
                        "length": self.ajacentMatrix[startNodeIndex][endNodeIndex]
                    }
                    self.edges.append(edgeDict)
        self.edges = sorted(self.edges, key=lambda k: k["length"])

    def find(self, x):
        if self.parent[x] != x:
            result = self.find(self.parent[x])
            self.parent[x] = result
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

    def allNodesIncluded(self):
        rootNodesList = [self.find(eachNode) for eachNode in self.nodes]
        if len(set(rootNodesList)) == 1:
            return True
        else:
            return False

    def run(self):
        minSpanningTree = []
        for eachEdgeDict in self.edges:
            if self.find(eachEdgeDict["startNodeIndex"]) != self.find(eachEdgeDict["endNodeIndex"]):
                self.merge(eachEdgeDict["startNodeIndex"], eachEdgeDict["endNodeIndex"])
                minSpanningTree.append(eachEdgeDict)
            if self.allNodesIncluded():
                print(f"minimun spanning tree is {minSpanningTree}")
                return
        print(f"Error, Couldn't generate a minimum spanning tree...")


instance = KrusKaAlogrithm()
instance.run()

