import sys

MAXN = 5000 + 5
sys.setrecursionlimit(MAXN)


# disjoint set
class Dsu:
    def __init__(self, size):
        self.parent = []


n, m, p = map(int, input().strip().split())
