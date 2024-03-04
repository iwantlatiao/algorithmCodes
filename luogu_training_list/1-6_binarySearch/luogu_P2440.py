def check(x):
    cnt = 0
    for l in logLen:
        cnt += l // x
    if cnt >= k:
        return True
    else:
        return False


n, k = map(int, input().split())
logLen = []
for i in range(n):
    logLen.append(int(input()))

if sum(logLen) < k:
    print("0")
else:
    l, r = 1, max(logLen)
    while l < r:
        mid = (l + r) >> 1
        if check(mid):
            l = mid + 1
        else:
            r = mid
    if check(r) == False:
        r -= 1
    print(r)
