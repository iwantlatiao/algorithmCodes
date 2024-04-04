import sys
from bisect import bisect_left

input = sys.stdin.readline

l = [-2147483647, 2147483647]
q = int(input())
for i in range(q):
    op, x = map(int, input().split())
    # 查询 x 的排名 ( 比 x 小的数的数量 )
    if op == 1:
        ans = bisect_left(l, x)
        print(ans)
    # 查询排名为 x 的数
    elif op == 2:
        print(l[x])
    # 求 x 的前驱
    elif op == 3:
        pos = bisect_left(l, x)
        print(l[pos - 1])
    # 求 x 的后继
    elif op == 4:
        pos = bisect_left(l, x)
        if l[pos] == x:
            print(l[pos + 1])
        else:
            print(l[pos])
    # 插入 x
    elif op == 5:
        pos = bisect_left(l, x)
        l.insert(pos, x)
