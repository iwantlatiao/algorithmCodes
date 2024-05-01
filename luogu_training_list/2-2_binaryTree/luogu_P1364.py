import sys

MAXN = 100 + 5
sys.setrecursionlimit(MAXN)


class EdgeStruct:
    def __init__(self) -> None:
        self.to = -1
        self.next = -1


# 在 u -> v 建一条边
def addEdge(u, v):
    e = EdgeStruct()
    e.to, e.next = v, head[u]
    edge.append(e)
    head[u] = len(edge) - 1


# 第一次 dfs 计算代价, 可以从任意点开始, 这里选择根节点为 1
def dfs1(fa, u, dep):
    size[u] = num[u]  # 这里求子树大小是为了后面 DP 使用
    i = head[u]
    while i != -1:
        if edge[i].to != fa:
            dfs1(u, edge[i].to, dep + 1)
            size[u] += size[edge[i].to]
        i = edge[i].next
    f[1] += num[u] * dep


# 第二次 dfs 为换根 DP
def dfs2(fa, u):
    i = head[u]
    while i != -1:
        if edge[i].to != fa:
            v, treeSize = edge[i].to, size[1]
            f[v] = f[u] + treeSize - (size[v] << 1)
            dfs2(u, v)
        i = edge[i].next


# 邻接表
edge = []
head = [-1 for _ in range(MAXN)]

# 点权
num = [0 for _ in range(MAXN)]

# 以 1 为根的子树的大小
size = [0 for _ in range(MAXN)]

# 换根 DP 使用的递推数组
f = [0 for _ in range(MAXN)]

n = int(input().strip())
for i in range(1, n + 1):
    w, u, v = map(int, input().strip().split())
    num[i] = w
    if u > 0:
        addEdge(i, u), addEdge(u, i)
    if v > 0:
        addEdge(i, v), addEdge(v, i)

dfs1(1, 1, 0)
dfs2(1, 1)

print(min(f[1 : n + 1]))
