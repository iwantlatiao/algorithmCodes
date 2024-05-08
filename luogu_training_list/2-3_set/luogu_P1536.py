import sys

MAXN = 1000 + 5
sys.setrecursionlimit(MAXN)


class Dsu:
    def __init__(self, size) -> None:
        self.parent = list(range(size))
        self.size = [1 for _ in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return x
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]


while True:
    s = input().strip().split()
    if len(s) == 2:
        n, m = map(int, s)
        dsu = Dsu(n + 1)
        for _ in range(m):
            x, y = map(int, input().strip().split())
            dsu.union(x, y)
        ans = 0
        for i in range(1, n + 1):
            if i == dsu.find(i):
                ans += 1
        print(ans - 1)
    else:
        break
