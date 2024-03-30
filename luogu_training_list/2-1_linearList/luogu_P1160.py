MAXN = 100005
l = [[-1, -1, -1] for _ in range(MAXN)]  # pre, next, number
num = [0 for _ in range(MAXN)]  # i 同学现在的节点为 l[num[i]]
l[0], l[1], num[1] = [-1, 1, 0], [0, -1, 1], 1
cnt = 1


def insert(i, k, dir):
    global cnt
    cnt += 1
    l[cnt] = [-1, -1, i]
    num[i] = cnt
    # 插入左侧
    if dir == 0:
        # i 号同学的左边同学节点为 l[preIndex]
        preIndex = l[num[k]][0]
        l[num[k]][0] = cnt
        l[preIndex][1] = cnt
        l[cnt][0:2] = [preIndex, num[k]]
    else:
        # i 号同学的左边同学节点为 l[nxtIndex]
        nxtIndex = l[num[k]][1]
        l[num[k]][1] = cnt
        l[cnt][0:2] = [num[k], nxtIndex]
        if nxtIndex != -1:
            l[nxtIndex][0] = cnt


def delete(x):
    if num[x] != -1:
        preIndex, nxtIndex = l[num[x]][0], l[num[x]][1]
        l[num[x]] = [-1, -1, -1]
        l[preIndex][1] = nxtIndex
        if nxtIndex != -1:
            l[nxtIndex][0] = preIndex
        num[x] = -1


if __name__ == "__main__":
    N = int(input())
    for i in range(2, N + 1):
        k, p = map(int, input().split())
        insert(i, k, p)  # 把 i 同学插到 k 同学的 p 侧
    M = int(input())
    for i in range(M):
        x = int(input())
        delete(x)

    x = l[0]
    while x[2] != -1:
        if x[2] != 0:
            print(x[2], end=" ")
        x = l[x[1]]
