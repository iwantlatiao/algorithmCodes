import sys
from bisect import bisect_left

MAXN = 100000 + 5
sys.setrecursionlimit(MAXN)
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    l = []
    d = []  # 用于离散化的临时数组
    index = []  # 用于离散化的数组
    n = int(input().strip())
    for _ in range(n):
        i, j, e = map(int, input().strip().split())
        l.append([i, j, e])
        d.append(i), d.append(j)

    # 升序排序 然后去重 取索引作为离散化结果
    d.sort()
    if len(d) > 0:
        index.append(d[0])
        for i in range(1, len(d)):
            if d[i - 1] != d[i]:
                index.append(d[i])
    for i in range(len(l)):
        x, y = l[i][0], l[i][1]
        x, y = bisect_left(index, x), bisect_left(index, y)
        l[i][0], l[i][1] = x, y
