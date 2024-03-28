from math import sqrt


N, MAXD = 16, 1000 * 16
cheese = []  # 奶酪的坐标
dis = [[0 for _ in range(N)] for _ in range(N)]  # 两两奶酪之间的距离
dis_s = []  # 起点到奶酪的距离
# f[i][j] 表示当前位置 i 状态 j 的最小距离
f = [[MAXD for _ in range(1 << N)] for _ in range(N)]


# 求两两奶酪之间的距离
def distanceInit():
    for i in range(n):
        x1, y1 = cheese[i][0], cheese[i][1]
        dis_s.append(sqrt(x1 * x1 + y1 * y1))
        for j in range(i):
            x2, y2 = cheese[j][0], cheese[j][1]
            dis[i][j] = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            dis[j][i] = dis[i][j]
    for i in range(n):
        f[i][1 << i] = dis_s[i]


# 三层循环, 最外层遍历当前状态,
# 第二层遍历当前位置, 第三层遍历前一个位置.
def DP():
    for i in range(1, 1 << n):
        for j in range(n):
            # 该状态没走过当前位置就跳过
            if i & (1 << j) == 0:
                continue
            for k in range(n):
                # 该状态没走过前一个位置 或 前一个位置和当前位置相同 就跳过
                if i & (1 << k) == 0 or j == k:
                    continue
                f[j][i] = min(f[j][i], f[k][i - (1 << j)] + dis[k][j])


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        cheese.append(list(map(float, input().split())))
    distanceInit()
    DP()

    ans = MAXD
    for i in range(n):
        ans = min(ans, f[i][(1 << n) - 1])

    print("{:.2f}".format(ans))
