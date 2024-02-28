from bisect import bisect_left
import sys

# 快速读入, 但是好像并不是很快
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
num = list(map(int, input().split()))
query = map(int, input().split())

for q in query:
    i = bisect_left(num, q)
    if i == len(num) or num[i] != q:  # 注意判断超出右边界
        print("-1", end=" ")
    else:
        print(i + 1, end=" ")
