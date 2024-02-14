CDir = [
    [0, 0],
    [2, 1],
    [1, 2],
    [-1, 2],
    [-2, 1],
    [-2, -1],
    [-1, -2],
    [1, -2],
    [2, -1],
]
MAXB = 22


def search(x, y):
    if x < 0 or y < 0 or x > B[0] or y > B[1]:  # 超出范围
        return 0
    elif num[x][y] == -1:  # 不能走的格子
        return 0
    elif num[x][y] != 0:  # 之前计算过
        return num[x][y]
    else:
        num[x][y] = search(x - 1, y) + search(x, y - 1)
        return num[x][y]


l = list(map(int, input().split()))
B, C = l[:2], l[2:4]

num = [[0 for _ in range(MAXB)] for _ in range(MAXB)]
num[0][0] = 1
for i in range(9):
    cx, cy = C[0] + CDir[i][0], C[1] + CDir[i][1]
    if 0 <= cx and cx <= B[0] and 0 <= cy and cy <= B[1]:
        num[cx][cy] = -1

print(search(B[0], B[1]))
