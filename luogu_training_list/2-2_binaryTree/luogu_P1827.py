import sys

sys.setrecursionlimit(1000000)


def dfs(inOrder: str, preOrder: str):
    root = preOrder[0]
    rootIndex = inOrder.find(root)  # 中序遍历 根的位置

    # 如果有左子树就遍历左子树
    if rootIndex > 0:
        dfs(inOrder[:rootIndex], preOrder[1 : rootIndex + 1])

    # 如果有右子树就遍历右子树
    if rootIndex < len(inOrder) - 1:
        dfs(inOrder[rootIndex + 1 :], preOrder[rootIndex + 1 :])

    print(root, end="")


input = sys.stdin.readline
inOrder = input().strip()
preOrder = input().strip()
dfs(inOrder, preOrder)
