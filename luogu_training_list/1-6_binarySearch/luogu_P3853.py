def check(x):
    i, j, cnt = 0, 1, 0
    while j < len(sign):
        if sign[j] - sign[i] < x:
            if cnt < K and j < len(sign) - 1:  # take j-th sign
                j += 1
                cnt += 1
            elif cnt < K and j == len(sign) - 1:  # take i-th sign
                break
            else:
                return False
        else:
            i = j
            j = i + 1
    return True


L, N, K = map(int, input().split())
sign = [0]
for _ in range(N):
    sign.append(int(input()))
sign.append(L)

l, r = 1, sign[len(sign) - 1]
while l < r:
    mid = (l + r) >> 1
    if check(mid):
        l = mid + 1
    else:
        r = mid

if check(l) == False:
    l -= 1

print(l)
