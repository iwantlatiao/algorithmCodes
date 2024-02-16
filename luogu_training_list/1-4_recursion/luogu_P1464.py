MAXNUM = 22
f = [[[0 for i in range(MAXNUM)] for i in range(MAXNUM)] for i in range(MAXNUM)]


def search(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    if x > 20 or y > 20 or z > 20:
        return search(20, 20, 20)
    if f[x][y][z] > 0:
        return f[x][y][z]
    if x < y and y < z:
        f[x][y][z] = search(x, y, z - 1) + search(x, y - 1, z - 1) - search(x, y - 1, z)
    else:
        f[x][y][z] = (
            search(x - 1, y, z)
            + search(x - 1, y - 1, z)
            + search(x - 1, y, z - 1)
            - search(x - 1, y - 1, z - 1)
        )
    return f[x][y][z]


a, b, c = map(int, input().split())
while a != -1 or b != -1 or c != -1:
    print("w({}, {}, {}) = {}".format(a, b, c, search(a, b, c)))
    a, b, c = map(int, input().split())
