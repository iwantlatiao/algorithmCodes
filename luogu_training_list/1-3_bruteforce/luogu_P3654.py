R, C, K = map(int, input().split())
m = []
for i in range(R):
    m.append(input())

ans = 0
# 扫描第 i 行的连续空位
for i in range(R):
    empty = 0
    for j in range(C):
        if m[i][j] == ".":
            empty += 1
            if empty >= K:
                ans += 1
        else:
            empty = 0

# 扫描第 j 列的连续空位
for j in range(C):
    empty = 0
    for i in range(R):
        if m[i][j] == ".":
            empty += 1
            if empty >= K:
                ans += 1
        else:
            empty = 0

if K == 1:
    ans //= 2

print(ans)
