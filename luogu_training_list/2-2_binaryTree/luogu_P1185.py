MAXM = 10 + 2
MAXWIDTH, MAXHEIGHT = 3100, 1600  # 打表估算可得

m, n = map(int, input().strip().split())

# branchLen[i]: 第 i 层的树枝长度,
# 即连接第 i 层与第 i+1 层树枝的长度,
# 可以通过前 i-1 层树枝之和 与 节点数得到
# pos[i]: 第 i 层节点的第一个节点的水平位置
# h[i]: 第 i 层节点的竖直位置
branchLen = [0 for _ in range(MAXM)]
pos = [0 for _ in range(MAXM)]
h = [0 for _ in range(MAXM)]
branchLen[1], pos[1] = 1, 1  # 第一层树枝长 1
for i in range(2, m + 1):
    branchLen[i] = (i - 1) + sum(branchLen[1:i])
    pos[i] = branchLen[i] + 1

h[m] = 1  # 最顶上那层竖直位置为 1
for i in range(m - 1, 0, -1):
    h[i] = h[i + 1] + branchLen[i] + 1

ch = [[" " for _ in range(MAXWIDTH)] for _ in range(MAXHEIGHT)]


def draw(x, y, depth):
    ch[x][y] = "o"
    if depth == 1:
        return
    lx, ly, rx, ry = x + 1, y - 1, x + 1, y + 1
    for i in range(branchLen[depth - 1]):
        ch[lx][ly], ch[rx][ry] = "/", "\\"
        lx, ly, rx, ry = lx + 1, ly - 1, rx + 1, ry + 1
    draw(lx, ly, depth - 1), draw(rx, ry, depth - 1)


def delete(x, y):
    ch[x][y] = " "
    if ch[x - 1][y - 1] == "\\":
        delete(x - 1, y - 1)
    if ch[x - 1][y + 1] == "/":
        delete(x - 1, y + 1)
    if ch[x + 1][y - 1] == "/" or ch[x + 1][y - 1] == "o":
        delete(x + 1, y - 1)
    if ch[x + 1][y + 1] == "\\" or ch[x + 1][y + 1] == "o":
        delete(x + 1, y + 1)


draw(1, pos[m], m)
for _ in range(n):
    layer, i = map(int, input().strip().split())
    layer = m - layer + 1
    if layer == 1:
        if i & 1 == 1:  # 奇数个
            delete(h[layer], 3 * (i - 1) + 1)
        else:
            delete(h[layer], 3 * (i - 2) + 5)
    else:
        delete(h[layer], pos[layer] + (i - 1) * (2 * branchLen[layer] + 2))

height, width = h[1], 3 * (1 << m)
for i in range(1, height + 1):
    print("".join(ch[i][1 : width + 1]))
