MAXNUM = 1000000000
N = int(input())
s, b = [], []
for _ in range(N):
    x, y = map(int, input().split())
    s.append(x)
    b.append(y)


def search(curD, curS, curB, used):
    if curD >= N - 1:
        if used >= 1:
            global ans
            ans = min(ans, abs(curS - curB))
        return
    search(curD + 1, curS, curB, used)
    search(curD + 1, curS * s[curD + 1], curB + b[curD + 1], used + 1)


ans = MAXNUM

search(0, 1, 0, 0)
search(0, s[0], b[0], 1)

print(ans)
