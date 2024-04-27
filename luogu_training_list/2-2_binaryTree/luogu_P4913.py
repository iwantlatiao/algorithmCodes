import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
tree = [[0, 0]]
n = int(input().strip())
ans, h = 0, 0


# 当前节点为 x, 高度为 h
def dfs(x):
    global ans, h
    if x == 0:
        ans = max(ans, h)
        return

    h += 1
    # 遍历左右儿子
    for i in range(2):
        dfs(tree[x][i])
    h -= 1


for i in range(n):
    l, r = map(int, input().split())
    tree.append([l, r])

dfs(1)
print(ans)
