import random


# 基于三路快排的 nth element
def quickSort(left, right):
    if left >= right:
        return
    randomIndex = random.randint(left, right)
    pivot = arr[randomIndex]
    arr[left], arr[randomIndex] = arr[randomIndex], arr[left]
    i = left + 1  # 扫描索引
    lt = left  # 小于 pivot 在 [left,lt-1]
    gt = right + 1  # 大于 pivot 在 [gt,right]
    while i < gt:
        if arr[i] < pivot:
            arr[i], arr[lt + 1] = arr[lt + 1], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt - 1] = arr[gt - 1], arr[i]
            gt -= 1
        else:
            i += 1
    arr[left], arr[lt] = arr[lt], arr[left]
    if k < lt:
        quickSort(arr, left, lt - 1)
    elif k >= gt:
        quickSort(arr, gt, right)
    else:
        print(arr[k])
        exit(0)


n, k = map(int, input().split())
# num = [int(s) for s in input().split()]

import numpy as np

# print(np.partition(np.fromstring(input(),dtype=np.int32,sep=' '),k)[k])

arr = np.fromstring(input(), dtype=np.int32, sep=" ")

quickSort(0, n - 1)
