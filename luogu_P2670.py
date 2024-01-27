n, m = map(int, input().split())

# 地图的范围是(1,1)~(n,m)，围上一圈"?"
x = [["?" for _ in range(m + 2)]]
for i in range(n):
    s = list(input())
    x.append(["?"] + s + ["?"])
x.append(["?" for _ in range(m + 2)])

# (i,j) 是当前需要计算的坐标
# (i+di,j+dj) 是正在扫描的坐标
ans = [[0 for _ in range(m)] for _ in range(n)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if x[i][j] == "*":
            ans[i - 1][j - 1] = -1
            continue
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if (di == 0) and (dj == 0):
                    continue
                if x[i + di][j + dj] == "*":
                    ans[i - 1][j - 1] += 1

for i in range(n):
    for j in range(m):
        if ans[i][j] == -1:
            print("*", sep="", end="")
        else:
            print(ans[i][j], sep="", end="")
    print()
