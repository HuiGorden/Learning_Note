#!python3

# Calculate Binomial Coefficient
# Relation: C(n,k) = C(n-1, k-1) + C(n-1, k)
#           C(n,k) = 1 if k = 0 or n=k
def calculateBinomialCoefficient(n, k):
    result = [["*" for i in range(n + 1)] for i in range(n + 1)]
    result[0][0] = 1
    for i in range(1, n + 1):
        for j in range(0, min(i, k) + 1):
            if j == 0 or j == i:
                result[i][j] = 1
            else:
                result[i][j] = result[i-1][j-1] + result[i-1][j]
    return result, result[n][k]


def outputMatrix(matrix):
    [print(" ".join([str(element) for element in inner])) for inner in matrix]


resultMatrix, result = calculateBinomialCoefficient(4, 2)
print(f"Result is:{result}")
outputMatrix(resultMatrix)
