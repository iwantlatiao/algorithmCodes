# center coordinate (x,y); size r
def rotate_arr(x, y, r, z):
    startX, startY = x - r, y - r
    endX, endY = x + r, y + r
    arr_size = 2 * r + 1
    # numpy can do while list can't:
    # tmp_arr = arr[startX : endX + 1, startY : endY + 1]
    tmp_arr = [
        [arr[i][j] for j in range(startY, endY + 1)] for i in range(startX, endX + 1)
    ]

    # anti-clockwise
    if z == 1:
        rotated_arr = [
            [tmp_arr[j][2 * r - i] for j in range(arr_size)] for i in range(arr_size)
        ]
    else:
        rotated_arr = [
            [tmp_arr[2 * r - j][i] for j in range(arr_size)] for i in range(arr_size)
        ]
    # arr[startX : endX + 1][startY : endY + 1] = rotated_arr
    for i in range(startX, endX + 1):
        for j in range(startY, endY + 1):
            arr[i][j] = rotated_arr[i - startX][j - startY]


n, m = map(int, input().split())
arr = [[n * i + j for j in range(1, n + 1)] for i in range(n)]

for _ in range(m):
    x, y, r, z = map(int, input().split())
    if r > 0:
        rotate_arr(x - 1, y - 1, r, z)

for i in range(n):
    for j in range(n - 1):
        print(arr[i][j], end=" ")
    print(arr[i][n - 1])
