from collections import deque


def solve():
    MAXN = 100005
    ans = 0

    n = int(input().strip())
    # q = [[arriveTime, nation]]
    q = deque()

    nation = [0 for _ in range(MAXN)]
    for _ in range(n):
        l = list(map(int, input().strip().split()))
        t, k = l[0], l[1]
        while len(q) > 0:
            u = q[0]
            # 如果这个人到达时间在 86400 秒之前, 就将其移出队尾
            if u[0] + 86400 <= t:
                q.popleft()
                nation[u[1]] -= 1
                if nation[u[1]] == 0:
                    ans -= 1
            else:
                break

        for i in range(k):
            x = l[i + 2]
            q.append([t, x])
            nation[x] += 1
            if nation[x] == 1:
                ans += 1

        print(ans)


solve()
