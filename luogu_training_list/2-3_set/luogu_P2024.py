import sys


class Dsu:
    def __init__(self, size) -> None:
        self.parent = list(range(size))
        self.size = [1 for _ in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x


MAXN = 50000 + 5
sys.setrecursionlimit(MAXN)
input = sys.stdin.readline

N, K = map(int, input().strip().split())
ans = 0
dsu = Dsu(3 * N + 1)
for _ in range(K):
    op, x, y = map(int, input().strip().split())
    if x > N or y > N:
        ans += 1
        continue
    if op == 1:  # x 和 y 是同类
        if dsu.find(x) == dsu.find(y + N) or dsu.find(y) == dsu.find(x + N):
            ans += 1
        else:
            dsu.union(x, y)  # A 种族的同类关系
            dsu.union(x + N, y + N)  # A 种族的猎物 B 种族的同类关系
            dsu.union(x + N + N, y + N + N)  # A 种族的天敌 C 种族的同类关系
    else:  # x 捕食 y
        if dsu.find(x) == dsu.find(y) or dsu.find(y) == dsu.find(x + N):
            ans += 1
        else:
            dsu.union(x, y + N)
            dsu.union(x + N, y + N + N)
            dsu.union(x + N + N, y)

print(ans)
