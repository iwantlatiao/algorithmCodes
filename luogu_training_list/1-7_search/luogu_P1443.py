from queue import Queue


MAXNUM = 400 + 10
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
n, m, x, y = map(int, input().split())
dis = [[-1 for _ in range(MAXNUM)] for _ in range(MAXNUM)]
q = Queue()
q.put((x, y))
dis[x][y] = 0

while q.empty() == False:
    curx, cury = q.get()
    for i in range(8):
        nxtx, nxty = curx + dx[i], cury + dy[i]
        if (
            1 <= nxtx
            and nxtx <= n
            and 1 <= nxty
            and nxty <= m
            and dis[nxtx][nxty] == -1
        ):
            dis[nxtx][nxty] = dis[curx][cury] + 1
            q.put((nxtx, nxty))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print("{:<5}".format(dis[i][j]), end="")
    print()
