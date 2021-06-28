#!python3

ajacentMatrix = [
    [0, 1, 3, float("inf"), float("inf")],
    [1, 0, 3, 6, float("inf")],
    [3, 3, 0, 4, 2],
    [float("inf"), 6, 4, 0, 5],
    [float("inf"), float("inf"), 2, 5, 0]
]
nodes = [f"V{i}" for i in range(len(ajacentMatrix))]


def Prim():
    totalCost = 0
    spanningTreeEdges = []
    nearest = ["V0" for i in range(len(ajacentMatrix))]
    distance = []
    for i in range(len(ajacentMatrix)):
        distance.append(ajacentMatrix[0][i])
    for time in range(len(nodes) - 1):
        minValue = float("inf")
        vnear = ""
        # pick which node add to spanning Tree this time
        for index in range(1, len(nodes)):
            if 0 < distance[index] < minValue:
                vnear = index
                minValue = distance[index]
        totalCost += minValue
        edge = f"({nearest[vnear]}, V{vnear})"
        spanningTreeEdges.append(edge)
        distance[vnear] = -1
        for index in range(1, len(nodes)):
            if ajacentMatrix[index][vnear] < distance[index]:
                distance[index] = ajacentMatrix[index][vnear]
                nearest[index] = f"V{vnear}"
    print(f"Min Spanning Tree cost: {totalCost}")
    print(f"Min Spanning Tree contains edges: {' '.join(spanningTreeEdges)}")


Prim()
