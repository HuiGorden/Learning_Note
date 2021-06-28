#!python3

example = [27, 10, 12, 20, 25, 13, 15, 22]


def merge(low, mid, high):
    tmpData = []
    (left, right) = (low, mid + 1)
    while left <= mid and right <= high:
        if example[left] < example[right]:
            tmpData.append(example[left])
            left += 1
        else:
            tmpData.append(example[right])
            right += 1
    if left > mid:
        [tmpData.append(i) for i in example[right: high + 1]]
    else:
        [tmpData.append(i) for i in example[left: mid + 1]]
    example[low:high + 1] = tmpData


def mergeSort(low, high):
    mid = int((low + high)/2)
    if low < high:
        mergeSort(low, mid)
        mergeSort(mid+1, high)
        merge(low, mid, high)


print(f"Origin: {example}")
mergeSort(0, len(example) - 1)
print(f"Change to: {example}")

