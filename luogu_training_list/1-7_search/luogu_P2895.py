from queue import Queue

MAXNUM = 300 + 5
road = [[-1 for _ in range(MAXNUM)] for _ in range(MAXNUM)]
dis = [[-1 for _ in range(MAXNUM)] for _ in range(MAXNUM)]
dx, dy = [1, 0, -1, 0, 0], [0, 1, 0, -1, 0]

M = int(input())
for _ in range(M):
    x, y, t = map(int, input().split())
    for i in range(5):
        nxtx, nxty = x + dx[i], y + dy[i]
        if (
            0 <= nxtx
            and nxtx <= MAXNUM
            and 0 <= nxty
            and nxty <= MAXNUM
            and (road[nxtx][nxty] == -1 or t < road[nxtx][nxty])
        ):
            road[nxtx][nxty] = t

if road[0][0] == -1:
    print(0)
    exit(0)

q = Queue()
q.put((0, 0))
dis[0][0] = 0
found = False

while q.empty() == False:
    curx, cury = q.get()
    for i in range(4):
        nxtx, nxty = curx + dx[i], cury + dy[i]
        # 走到 (300, 300) 外也可以
        if 0 <= nxtx and 0 <= nxty and dis[nxtx][nxty] == -1:
            if road[nxtx][nxty] == -1:
                print(dis[curx][cury] + 1)
                exit(0)
            elif dis[curx][cury] + 1 < road[nxtx][nxty]:
                dis[nxtx][nxty] = dis[curx][cury] + 1
                q.put((nxtx, nxty))

print(-1)
