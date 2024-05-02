import sys
from collections import deque
from math import log2

MAXN = 100 + 5
sys.setrecursionlimit(MAXN)
input = sys.stdin.readline
edge, head = [], [-1 for _ in range(MAXN)]
depth = [0 for _ in range(MAXN)]  # 各节点的深度
width = [0 for _ in range(MAXN)]  # 各深度的宽度
# 倍增. f[i,j] 表示第 i 个节点往上 2^j 的祖先
f = [[0 for _ in range(10 + int(log2(MAXN)))] for _ in range(MAXN)]


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


# 对 f 数组进行递推, 步骤:
# 1. 根节点入队, 存储深度 d
# 2. 取出队头, 遍历所有出边 (跳过父亲的边) , 处理出边的点的 d 和 f ,
#    其中 f[i][j] = f[ f[i][j-1] ][j-1]
# 3. 重复第 2 步直到队空
def bfsPreprocess():
    q = deque()
    # 1 号节点为根
    q.append(1)
    depth[1], width[1] = 1, 1
    while len(q) > 0:
        x = q.popleft()
        i = head[x]
        while i != -1:
            y = edge[i].to
            # 如果该点已经被遍历过 (父亲节点) 就跳过
            if depth[y] == 0:
                depth[y] = depth[x] + 1
                width[depth[y]] += 1
                f[y][0] = x
                # 更精确的, 应该是 0 ~ int(log2(depth[y] - depth[root])) + 1
                # 跳过头的结果都是 0
                for j in range(1, lgn + 1):
                    f[y][j] = f[f[y][j - 1]][j - 1]
                q.append(y)
            i = edge[i].next


# 求出两点 x, y 之间的 LCA, 步骤:
# 1. 先让 d[x] < d[y], 如果不是就先交换
# 2. 让 y 上移 (二进制拆分) 到与 x 相同的深度,
#    若此时 x = y 就说明 LCA(x,y) = 当前节点
# 3. 再用二进制拆分把 x 和 y 同时上移, 并且保证 x != y.
#    完成该步后, x 和 y 一定在某个节点的两个子节点上,
#    因此 LCA(x,y) = 他们的父亲节点
def lca(x, y):
    if depth[x] > depth[y]:
        x, y = y, x
    # 从 logn 到 0 上移
    for i in range(lgn, -1, -1):
        if depth[f[y][i]] >= depth[x]:
            y = f[y][i]
    if x == y:
        return x
    for i in range(lgn, -1, -1):
        if f[x][i] != f[y][i]:
            x, y = f[x][i], f[y][i]
    return f[x][0]


n = int(input().strip())
lgn = int(log2(n))

for i in range(n - 1):
    u, v = map(int, input().strip().split())
    addEdge(u, v), addEdge(v, u)

x, y = map(int, input().strip().split())

bfsPreprocess()

print(max(depth))
print(max(width))

ansestor = lca(x, y)

print(2 * (depth[x] - depth[ansestor]) + (depth[y] - depth[ansestor]))
