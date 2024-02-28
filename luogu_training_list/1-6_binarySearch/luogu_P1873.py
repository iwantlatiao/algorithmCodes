def cal(x):  # 得到的木材高度
    cut = 0
    for t in h:
        if t > x:
            cut += t - x
    return cut


def bS(l, r):
    # res[:r] > M, res[r] <= M
    if l == r:
        if cal(l) >= M:
            return l
        else:
            return l - 1
    mid = (l + r) >> 1
    res = cal(mid)
    if res <= M:  # 不够
        return bS(l, mid)  # 砍多点
    else:
        return bS(mid + 1, r)


N, M = map(int, input().split())
h = list(map(int, input().split()))

print(bS(0, max(h)))
