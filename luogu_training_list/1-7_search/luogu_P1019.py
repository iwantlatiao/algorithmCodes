N, ans = 22, 0
str = []
add = [[0 for _ in range(N)] for _ in range(N)]
used = [2 for _ in range(N)]


# 处理字符串 str[x] 和 str[y] 相连增加的长度
def pre(x, y):
    x, y = str[x], str[y]
    for ml in range(1, min(len(x), len(y)) + 1):
        u, v = x[len(x) - ml :], y[:ml]
        res = 1
        for i in range(ml):
            if u[i] != v[i]:
                res = 0
                break
        if res == 1:
            return len(y) - ml
    return 0


# 最后使用的单词 总长度
def dfs(x, sum):
    global ans
    ans = max(ans, sum)
    for i in range(n):
        # 仅当 没用过 2 次 且 能接龙 才继续搜索
        if used[i] > 0 and add[x][i] > 0:
            used[i] -= 1
            dfs(i, sum + add[x][i])
            used[i] += 1


if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        str.append(input().strip())
    for i in range(n):
        for j in range(n):
            add[i][j] = pre(i, j)
    startChar = input().strip()
    for i in range(n):
        if str[i][0] == startChar:
            used[i] -= 1
            dfs(i, len(str[i]))
            used[i] += 1
    print(ans)
