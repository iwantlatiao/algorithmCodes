from queue import Queue

MAXNUM = 200 + 10
dis = [-1 for _ in range(MAXNUM)]

N, A, B = map(int, input().split())

if A == B:
    print("0")
    exit(0)

K = list(map(int, input().split()))
K = [0] + K
q = Queue()
q.put((A))
dis[A] = 0

while q.empty() == False and dis[B] == -1:
    curL = q.get()

    nxtL = curL - K[curL]
    if nxtL >= 1 and dis[nxtL] == -1:
        q.put(nxtL)
        dis[nxtL] = dis[curL] + 1

    nxtL = curL + K[curL]
    if nxtL <= N and dis[nxtL] == -1:
        q.put(nxtL)
        dis[nxtL] = dis[curL] + 1

print(dis[B])
