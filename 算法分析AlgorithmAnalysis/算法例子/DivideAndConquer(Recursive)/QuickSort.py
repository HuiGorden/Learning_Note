#!python3

# example = [27, 10, 12, 20, 25, 13, 15, 22]
example = [15, 22, 13, 27, 12, 10, 20, 25]


def patition(low, high, pivotPoint):
    pivotItem = example[pivotPoint]
    for i in range(low+1, high+1):
        if pivotItem > example[i]:
            pivotPoint += 1
            tmp = example[pivotPoint]
            example[pivotPoint] = example[i]
            example[i] = tmp
    tmp = example[pivotPoint]
    example[pivotPoint] = pivotItem
    example[low] = tmp
    return pivotPoint


def quickSort(low, high):
    pivotPoint = low
    if high > low:
        pivotPoint = patition(low, high, pivotPoint)
        quickSort(low, pivotPoint-1)
        quickSort(pivotPoint + 1, high)


print(f"Origin: {example}")
quickSort(0, len(example) - 1)
print(f"Change to: {example}")

