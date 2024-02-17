MAXNUM = 102
MAXMONEY = 10002
N, M = map(int, input().split())
cost = list(map(int, input().split()))
f = [[0 for _ in range(MAXMONEY)] for _ in range(MAXNUM)]


# f[i][j] 表示对于前 i 个菜,
# 当前选第 i 个菜, 口袋剩 j 元时有多少种方案
def search(x, y):
    if f[x][y] > 0:
        return f[x][y]
    if y < 0:  # 没钱了
        return 0
    if y == 0:
        return 1
    for i in range(x):
        f[x][y] += search(i, y - cost[i])
    return f[x][y]


ans = 0
for i in range(N):
    ans += search(i, M - cost[i])

print(ans)
