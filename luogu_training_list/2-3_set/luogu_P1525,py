import sys

MAXN = 20000 + 5
sys.setrecursionlimit(MAXN)
input = sys.stdin.readline


class Dsu:
    def __init__(self, size) -> None:
        self.parent = [i for i in range(size)]
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
        self.parent[y] = x
        self.size[x] += self.size[y]


N, M = map(int, input().strip().split())
dsu = Dsu(N * 2 + 5)
hate = [[0, 0, 0] for _ in range(M)]
for i in range(M):
    a, b, c = map(int, input().strip().split())
    hate[i] = [a, b, c]

hate.sort(key=lambda x: (-x[2]))
for i in range(M):  # in descending order
    a, b, c = hate[i]
    if dsu.find(a) == dsu.find(b):
        print(c)
        exit(0)
    else:
        dsu.union(a, b + N), dsu.union(a + N, b)
print("0")
