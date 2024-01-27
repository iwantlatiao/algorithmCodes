def rotate_arr(x, y, r, z):
    startX, startY = x - r, y - r
    endX, endY = x + r, y + r
    tmpArr = [
        [arr[i][j] for j in range(startY, startY + 1)]
        for i in range(startX, endX + 1)
    ]


n, m = map(int, input().split())
arr = [[n * i + j for j in range(1, n + 1)] for i in range(n)]


print(arr)
