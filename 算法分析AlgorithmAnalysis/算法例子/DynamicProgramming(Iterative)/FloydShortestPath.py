#!python3

# Calculate Shortest Path using Floyd algorithm
# Relation: D(k)[i][j] = minimum(D(k-1)[i][j], D(k-1)[i][k] + D(k-1)[k][j])
adjacentMatrix = [
    [0, 1, float("inf"), 1, 5],
    [9, 0, 3, 2, float("inf")],
    [float("inf"), float("inf"), 0, 4, float("inf")],
    [float("inf"), float("inf"), 2, 0, 3],
    [3, float("inf"), float("inf"), float("inf"), 0]
]
costMatrix = [[eachCol for eachCol in eachRow] for eachRow in adjacentMatrix]
PathMatrix = [[ -1 for eachCol in eachRow] for eachRow in adjacentMatrix]


def FloydAlgorithm():
    for k in range(0, len(adjacentMatrix)):
        for rowIndex in range(0, len(adjacentMatrix)):
            for colIndex in range(0, len(adjacentMatrix)):
                if costMatrix[rowIndex][k] + costMatrix[k][colIndex] < costMatrix[rowIndex][colIndex]:
                    costMatrix[rowIndex][colIndex] = costMatrix[rowIndex][k] + costMatrix[k][colIndex]
                    PathMatrix[rowIndex][colIndex] = k


def outputMatrix(matrix):
    [print(" ".join([str(element) for element in inner])) for inner in matrix]


def printPath(startPoint, endPoint):
    path = [endPoint]
    while PathMatrix[startPoint][endPoint] != -1:
        path.append(PathMatrix[startPoint][endPoint])
        endPoint = PathMatrix[startPoint][endPoint]
    path.append(startPoint)
    path.reverse()
    print(path)
    print("->".join([str(tmp) for tmp in path]))


# Calculate Cost
FloydAlgorithm()
outputMatrix(costMatrix)
outputMatrix(PathMatrix)
# Print out path
startPoint = 4
endPoint = 2
print(f"Cost from {startPoint} to {endPoint} is : {costMatrix[startPoint][endPoint]}")
printPath(4, 2)


