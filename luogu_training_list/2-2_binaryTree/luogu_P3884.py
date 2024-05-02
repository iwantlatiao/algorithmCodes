import sys
from collections import deque

MAXN = 100 + 5
sys.setrecursionlimit(MAXN)
input = sys.stdin.readline
edge, head = [], [-1 for _ in range(MAXN)]
depth = [0 for _ in range(MAXN)]  # 各节点的深度
width = [0 for _ in range(MAXN)]  # 各深度的宽度


class EdgeStruct:
    def __init__(self) -> None:
        self.to = -1
        self.next = -1

    def __init__(self, to, next) -> None:
        self.to = to
        self.next = next


def addEdge(u, v):
    edge.append(EdgeStruct(v, head[u]))
    head[u] = len(edge) - 1


def bfsPreprocess():
    q = deque()
    # 1 号节点为根
    q.append(1)
    depth[1], width[1] = 1, 1


n = int(input().strip())
for i in range(n):
    u, v = map(int, input().strip().split())
    addEdge(u, v), addEdge(v, u)

bfsPreprocess()

x, y = map(int, input().strip().split())
