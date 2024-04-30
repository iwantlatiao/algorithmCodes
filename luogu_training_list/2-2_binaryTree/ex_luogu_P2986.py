import sys

# input = sys.stdin.readline

f = open("luogu_training_list/2-2_binaryTree/P2986_5.in")
input = f.readline

MAXN = 100000 + 5
sys.setrecursionlimit(MAXN)


def center(fa, u):
    # u 的树尺寸 = 当前点权 + 子树的点权
    size[u] = cow[u]

    i = head[u]
    while i != -1:
        if edge[i][0] != fa:
            center(u, edge[i][0])
            size[u] += cow[edge[i][0]]
            maxSize[u] = max(maxSize[u], cow[edge[i][0]])
        i = edge[i][2]
    maxSize[u] = max(maxSize[u], totalCow - size[u])


def dfs(fa, u):
    i = head[u]
    while i != -1:
        if edge[i][0] != fa:
            dis[edge[i][0]] = dis[u] + edge[i][1]
            dfs(u, edge[i][0])
        i = edge[i][2]


N = int(input().strip())
totalCow = 0
edge = []  # ith edge = [to, weight, nextEdgeIndex]
head = [-1 for _ in range(MAXN)]  # 第 i 个点的第一条出边
cow = [0 for _ in range(MAXN)]
size = [0 for _ in range(MAXN)]  # 第 i 个点的树尺寸
maxSize = [0 for _ in range(MAXN)]  # 第 i 个点的子树大小最大值
dis = [0 for _ in range(MAXN)]  # 第 i 个点到重心的距离

# 点的编号 1 ~ N
for i in range(1, N + 1):
    cow[i] = int(input().strip())
    totalCow += cow[i]

for i in range(N - 1):
    e_from, e_to, e_w = map(int, input().split())
    edge.append([e_to, e_w, head[e_from]])
    head[e_from] = len(edge) - 1
    edge.append([e_from, e_w, head[e_to]])
    head[e_to] = len(edge) - 1

# 找重心
center(1, 1)
minSize, minIndex = maxSize[1], 1
for i in range(2, N + 1):
    if maxSize[i] < minSize:
        minSize = maxSize[i]
        minIndex = i

print(minIndex)

# 取重心点 然后跑一次 dfs
dfs(minIndex, minIndex)
ans = 0
for i in range(1, N + 1):
    ans += dis[i] * cow[i]

print(ans)

f.close()
