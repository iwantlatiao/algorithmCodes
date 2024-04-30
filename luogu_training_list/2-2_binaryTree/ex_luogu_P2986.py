import sys

input = sys.stdin.readline
sys.setrecursionlimit(200000)
MAXN = 100000 + 5


def center(fa, u):
    # u 的树尺寸 = 当前点权 + 子树的点权
    size[u] = cow[u]

    i = head[u]
    # while i!=-1:
    # center(u, )


N = int(input().strip())
edge = []  # edge[ith edge] = [to, weight, nextEdgeIndex]
head = [-1 for _ in range(MAXN)]  # 第 i 个点的第一条出边
cow = []
size = [0 for _ in range(MAXN)]  # 第 i 个点的树尺寸

for i in range(N):
    cow.append(int(input().strip()))

for i in range(N - 1):
    e_from, e_to, e_w = map(int, input().split())
    edge.append([e_to, e_w, head[e_from]])
    head[e_from] = len(edge) - 1
    edge.append([e_from, e_w, head[e_to]])
    head[e_to] = len(edge) - 1
