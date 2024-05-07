import sys

MAXN = 5000 + 5
sys.setrecursionlimit(MAXN)


# disjoint set
class Dsu:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1 for _ in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x  # 小的往大的合并
        self.size[x] += self.size[y]


n, m, p = map(int, input().strip().split())
dsu = Dsu(n + 1)
for _ in range(m):
    x, y = map(int, input().strip().split())
    dsu.union(x, y)
for _ in range(p):
    x, y = map(int, input().strip().split())
    if dsu.find(x) == dsu.find(y):
        print("Yes")
    else:
        print("No")
