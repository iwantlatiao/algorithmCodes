MAXNUM = 300 + 5
road = [[0 for _ in range(MAXNUM)] for _ in range(MAXNUM)]
dis = [[-1 for _ in range(MAXNUM)] for _ in range(MAXNUM)]
dx, dy = [1, 0, -1, 0, 0], [0, 1, 0, -1, 0]
M = int(input())
for _ in range(M):
    x, y, t = map(int, input().split())
    for i in range(5):
        nxtx, nxty = x + dx, y + dy
        if (
            0 <= nxtx
            and nxtx <= MAXNUM
            and 0 <= nxty
            and nxty <= MAXNUM
            and road[nxtx][nxty] == -1
        ):
            road[nxtx][nxty] = t
