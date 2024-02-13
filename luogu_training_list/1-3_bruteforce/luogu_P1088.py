N = int(input())
M = int(input())
a = list(map(int, input().split()))

for i in range(M):
    # 题目保证不超过手指表示范围，故此处没有特判
    j, k = N - 2, N - 1
    # 第一步 找最靠后的升序
    while 0 <= j and (not a[j] < a[j + 1]):
        j -= 1
    # 第二步 在 j 后面块中找比它大的最小数
    while j + 1 < k and (not a[j] < a[k]):
        k -= 1
    # 第三步 交换第 j k 位数后对第 j 位数后排序
    a[j], a[k] = a[k], a[j]
    j += 1
    k = N - 1
    while j < k:
        a[j], a[k] = a[k], a[j]
        j += 1
        k -= 1

for i in range(N):
    print(a[i], end=" ")
