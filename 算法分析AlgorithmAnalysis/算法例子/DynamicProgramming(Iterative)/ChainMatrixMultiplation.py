#!python3

# Calculate minimum multiplication in chain matrix multiplation
# Relation: M[i][j] = minimun(M[i][k] + M[k+1][j] + d(i-1)dkdj for i <= k <= j-1
# A0 = 5X2, A1 = 2X3, A2 = 3X4, A3 = 4X6, A4 = 6X7, A5 = 7X8
matrixDimension = [5, 2, 3, 4, 6, 7, 8]
matrixNumber = len(matrixDimension) - 1
M = [["*" for columnIndex in range(matrixNumber)] for rowIndex in range(matrixNumber)]
P = [["*" for columnIndex in range(matrixNumber)] for rowIndex in range(matrixNumber)]


def minMultiplation():
    for rowIndex in range(len(M)):
        M[rowIndex][rowIndex] = 0
    for diagonalIndex in range(1, matrixNumber):
        rowIndex = 0
        columnIndex = diagonalIndex
        while rowIndex <= matrixNumber - 1 and columnIndex <= matrixNumber - 1:
            k = rowIndex
            minValue = float("inf")
            while k <= columnIndex - 1:
                # outputMatrix(M)
                # print(f"rowIndex: {rowIndex}")
                # print(f"k: {k}")
                # print(f"k+1: {k+1}")
                # print(f"columnIndex: {columnIndex}")
                value = M[rowIndex][k] + M[k+1][columnIndex] + matrixDimension[rowIndex]*matrixDimension[k + 1]*matrixDimension[columnIndex + 1]
                # print(f"matrixDimension[k]: {matrixDimension[k]}")
                # print(f"matrixDimension[k + 1]: {matrixDimension[k + 1]}")
                # print(f"matrixDimension[columnIndex + 1]: {matrixDimension[columnIndex + 1]}")
                # print(f"value: {value}")
                if value < minValue:
                    minValue = value
                    P[rowIndex][columnIndex] = k
                k += 1
            M[rowIndex][columnIndex] = minValue
            rowIndex += 1
            columnIndex += 1
    print(f"M result is :")
    outputMatrix(M)
    print(f"P result is :")
    outputMatrix(P)


def outputMatrix(matrix):
    for inner in matrix:
        for element in inner:
            if len(str(element)) < 5:
                print(" "*(5-len(str(element))) + str(element), end="")
            else:
                print(str(element), end="")
        print("")


def GetOrder(startingPoint, endingPoint):
    if startingPoint == endingPoint:
        return f"A{startingPoint}"
    else:
        k = P[startingPoint][endingPoint]
        orderString = "("
        orderString += GetOrder(startingPoint, k)
        orderString += GetOrder(k+1, endingPoint)
        orderString += ")"
        return orderString


minMultiplation()
print(GetOrder(0, 5))

