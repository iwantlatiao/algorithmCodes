def quickSort(alist, first, last):
    if first >= last:
        return
    midValue = alist[first]
    low, high = first, last
    while low < high:
        while low < high and alist[high] >= midValue:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < midValue:
            low += 1
        alist[high] = alist[low]
    alist[low] = midValue

    quickSort(alist, first, low - 1)
    quickSort(alist, low + 1, last)


N = int(input())
num = [int(s) for s in input().split()]

# quickSort(num, 0, N - 1)  # This will be TLE

num.sort()

for i in range(N):
    print(num[i], end=" ")
