cowMap = []
coWCoor = [0, 0, 0]  # x, y, dir
farmerCoor = [0, 0, 0]  # dir: up, right, down, left
moveX = [-1, 0, 1, 0]
moveY = [0, 1, 0, -1]

# farmer.x + farmer.y * 10 + cow.x * 100 + cow.y * 1000 +
# farmer.dir * 10000 + cow.dir * 40000
boolMap = [False for _ in range(170000)]


def move(curX, curY, curDir):
    nextX = curX + moveX[curDir]
    nextY = curY + moveY[curDir]
    if cowMap[nextX][nextY] != "*":
        return nextX, nextY, curDir
    else:
        curDir = (curDir + 1) % 4
        return curX, curY, curDir


cowMap.append(["*" for _ in range(12)])

for i in range(10):  # 1 ~ 10
    s = list(input().split()[0])
    for j in range(10):
        if s[j] == "C":
            coWCoor = [i + 1, j + 1, 0]
            break
        elif s[j] == "F":
            farmerCoor = [i + 1, j + 1, 0]
    cowMap.append(["*"] + s + ["*"])

cowMap.append(["*" for _ in range(12)])

for nowTime in range(160005):
    if coWCoor[0] == farmerCoor[0] and coWCoor[1] == farmerCoor[1]:
        print(nowTime)
        quit(0)

    boolMapValue = (
        farmerCoor[0]
        + farmerCoor[1] * 10
        + coWCoor[0] * 100
        + coWCoor[1] * 1000
        + farmerCoor[2] * 10000
        + coWCoor[2] * 40000
    )

    if boolMap[boolMapValue]:
        print("0")
        quit(0)
    else:
        boolMap[boolMapValue] = True

    coWCoor = move(coWCoor[0], coWCoor[1], coWCoor[2])
    farmerCoor = move(farmerCoor[0], farmerCoor[1], farmerCoor[2])


print("0")

"""
Test Data:
.****...*.
..*......*
*.........
..........
*........*
*.**.*..**
F..*......
***....*.*
.C.......*
.......*.*

Answer:58
"""
