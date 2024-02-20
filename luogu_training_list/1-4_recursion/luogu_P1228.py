# ox, oy: obstacle x, y
# x, y: current maze top left coordinate
# s: maze size
def search(ox, oy, x, y, s):
    if s <= 1:
        return
    s >>= 1
    # 障碍在左上角
    if ox - x < s and oy - y < s:
        print("{} {} 1".format(x + s, y + s))
        search(ox, oy, x, y, s)  # top left
        search(x + s - 1, y + s, x, y + s, s)  # top right
        search(x + s, y + s - 1, x + s, y, s)  # bottom left
        search(x + s, y + s, x + s, y + s, s)  # bottom right
    # 障碍在右上角
    elif ox - x < s and oy - y >= s:
        print("{} {} 2".format(x + s, y + s - 1))
        search(x + s - 1, y + s - 1, x, y, s)  # top left
        search(ox, oy, x, y + s, s)  # top right
        search(x + s, y + s - 1, x + s, y, s)  # bottom left
        search(x + s, y + s, x + s, y + s, s)  # bottom right
    # 障碍在左下角
    elif ox - x >= s and oy - y < s:
        print("{} {} 3".format(x + s - 1, y + s))
        search(x + s - 1, y + s - 1, x, y, s)  # top left
        search(x + s - 1, y + s, x, y + s, s)  # top right
        search(ox, oy, x + s, y, s)  # bottom left
        search(x + s, y + s, x + s, y + s, s)  # bottom right
    else:
        print("{} {} 4".format(x + s - 1, y + s - 1))
        search(x + s - 1, y + s - 1, x, y, s)  # top left
        search(x + s - 1, y + s, x, y + s, s)  # top right
        search(x + s, y + s - 1, x + s, y, s)  # bottom left
        search(ox, oy, x + s, y + s, s)  # bottom right


K = int(input())
X, Y = map(int, input().split())
search(X, Y, 1, 1, 1 << K)
