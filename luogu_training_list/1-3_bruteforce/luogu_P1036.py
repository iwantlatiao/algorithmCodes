import math


def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, 1 + int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True


def dfs(depth, choose, curSum):
    if depth >= N or choose > K:
        return
    if isPrime(curSum) and choose == K:
        global ans
        ans += 1
        return
    if depth + 1 < N:
        dfs(depth + 1, choose, curSum)
        if choose < K:
            dfs(depth + 1, choose + 1, curSum + x[depth + 1])


N, K = map(int, input().split())
x = [int(i) for i in input().split()]
ans = 0
dfs(0, 0, 0)
dfs(0, 1, x[0])

print(ans)
