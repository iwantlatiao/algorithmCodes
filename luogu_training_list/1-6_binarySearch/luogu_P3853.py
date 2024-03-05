def check(x):
    i, cnt, cur = 1, 0, sign[0]
    while i < len(sign):
        if sign[i] - cur > x:
            cur += x
            cnt += 1
        else:
            cur = sign[i]
            i += 1
        if cnt > K:
            return False
    if cnt <= K:
        return True


L, N, K = map(int, input().split())
sign = list(map(int, input().split()))

l, r = 1, sign[len(sign) - 1]
while l < r:  # check distance
    mid = (l + r) >> 1
    if check(mid) == False:
        l = mid + 1
    else:
        r = mid

if check(l) == False:
    l -= 1

print(l)
