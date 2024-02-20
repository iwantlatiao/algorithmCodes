MAXNUM = 2 + (1 << 11)
N = int(input())
s = [[" " for _ in range(MAXNUM)] for _ in range(MAXNUM)]
s[0][0], s[0][1], s[0][2], s[0][3] = "/", "_", "_", "\\"
s[1][0], s[1][1], s[1][2], s[1][3] = " ", "/", "\\", " "
lines = 4
rows = 2

for i in range(2, N + 1):
    # 横向复制
    lineStart, lineEnd = lines, lines << 1
    for j in range(rows):  # row
        s[j][lineStart:lineEnd] = s[j][0:lines]

    # 纵向复制
    lineStart, lineEnd = lines >> 1, (lines >> 1) + lines
    rowStart, rowEnd = rows, rows << 1
    for j in range(rowStart, rowEnd):  # row
        s[j][lineStart:lineEnd] = s[j - rows][0:lines]

    lines <<= 1
    rows <<= 1

for i in range(rows - 1, -1, -1):
    for j in range(lines):
        print(s[i][j], end="")
    print()
