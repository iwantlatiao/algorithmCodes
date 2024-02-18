N = int(input())
l = []
for _ in range(N):
    l.append("o")
for _ in range(N):
    l.append("*")
for _ in range(2):
    l.append("-")
length = (N << 1) + 2


def printMove():
    for i in range(length):
        print(l[i], end="")
    print()


def move(x, y):
    global l
    l[x], l[y] = l[y], l[x]
    l[x - 1], l[y - 1] = l[y - 1], l[x - 1]
    printMove()


def search(depth):
    if depth == 4:
        move(4, 9)
        move(8, 4)
        move(2, 8)
        move(7, 2)
        move(1, 7)
        return
    move(depth, (depth << 1) + 1)
    move((depth << 1) - 1, depth)
    search(depth - 1)


printMove()
search(N)
