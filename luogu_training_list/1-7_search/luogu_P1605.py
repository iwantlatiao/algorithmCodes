MAXN = 10
MAXT = 15
vis = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
count = 0
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]


# (x, y) 到 (FX, FY) 的方案数
def dfs(x, y):
    if x == FX and y == FY:
        global count
        count += 1
        return
    for i in range(4):
        nxtx, nxty = x + dx[i], y + dy[i]
        if 1 <= nxtx and nxtx <= N and 1 <= nxty and nxty <= M and vis[nxtx][nxty] == 0:
            vis[nxtx][nxty] = 1
            dfs(nxtx, nxty)
            vis[nxtx][nxty] = 0


if __name__ == "__main__":
    N, M, T = map(int, input().split())
    SX, SY, FX, FY = map(int, input().split())
    for _ in range(T):
        x, y = map(int, input().split())
        vis[x][y] = 1
    if vis[SX][SY] == 0 and vis[FX][FY] == 0:
        vis[SX][SY] = 1
        dfs(SX, SY)
    print(count)
