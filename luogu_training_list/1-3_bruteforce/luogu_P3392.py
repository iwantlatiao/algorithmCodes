N, M = map(int, input().split())
colors = []
for i in range(N):
    color = input()
    white, blue, red = 0, 0, 0
    for j in range(M):
        if color[j] == "W":
            white += 1
        elif color[j] == "B":
            blue += 1
        else:
            red += 1
    colors.append([white, blue, red])

ans = N * M

# 最上方 i (1 ~ N-2) 行的格子全部是白色的
for i in range(1, N - 1):
    # 接下来 j (1 ~ N-(i+1)) 行的格子全部是蓝色的
    for j in range(1, N - i):
        cur = 0
        # 剩下的 k 行是红色的
        k = N - i - j
        # 第 0 ~ i 行 的红色和蓝色染成白色
        for row in range(i):
            cur += colors[row][1] + colors[row][2]
        # 接下来 j 行 的红色和白色染成蓝色
        for row in range(i, i + j):
            cur += colors[row][0] + colors[row][2]
        # 接下来 k 行 的蓝色和白色染成红色
        for row in range(i + j, N):
            cur += colors[row][0] + colors[row][1]
        ans = min(ans, cur)

print(ans)
