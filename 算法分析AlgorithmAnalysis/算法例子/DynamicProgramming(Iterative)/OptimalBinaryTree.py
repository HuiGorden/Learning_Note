#!python3

# Calculate optimal binary tree, which make average searching time minimum


def outputMatrix(matrix):
    for eachRow in matrix:
        for element in eachRow:
            gap = 8 - len(str(element))
            print(f"{element}{' ' * gap}", end="")
        print("\n")


keys = ["Don", "Isabelle", "Ralph", "Wally"]
probability = [0, 0.375, 0.375, 0.125, 0.125]

A = [["*" for j in range(len(keys) + 1)] for i in range(len(keys) + 2)]
P = [["*" for j in range(len(keys) + 1)] for i in range(len(keys) + 2)]
for row in range(0, len(A)):
    for column in range(0, len(A[row])):
        if row == column + 1:
            A[row][column] = 0
        if row == column and row in range(1, len(keys) + 1):
            A[row][column] = probability[row]
for row in range(0, len(P)):
    for column in range(0, len(A[row])):
        if row == column and row in range(1, len(keys) + 1):
            P[row][column] = row
# initial
print(f"Before:\n")
outputMatrix(A)

for columnIndex in range(2, len(keys) + 1):
    row = 1
    column = columnIndex
    while column < len(keys) + 1:
        minValue = float("inf")
        cutPoint = ""
        for k in range(row, column):
            tmpOdds = 0
            if A[row][k - 1] + A[k+1][column] + sum(probability[row: column+1]) < minValue:
                cutPoint = k
                minValue = A[row][k - 1] + A[k+1][column] + sum(probability[row: column+1])
        A[row][column] = minValue
        P[row][column] = cutPoint
        row += 1
        column += 1

print(f"After A is :\n")
outputMatrix(A)
print(f"After P is :\n")
outputMatrix(P)
