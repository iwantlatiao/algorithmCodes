MAXNUM = 1000000000


def check(x):
    cnt, sum = 1, 0
    for i in range(len(num)):
        sum += num[i]
        if sum > x:
            sum = num[i]
            cnt += 1
        if cnt > M:
            return False
    return True


N, M = map(int, input().split())
num = list(map(int, input().split()))

l, r = max(num), sum(num)  # 注意搜索边界
while l < r:  # check maxsum
    mid = (l + r) >> 1
    if check(mid) == True:
        r = mid
    else:
        l = mid + 1

if check(l) == False:
    l -= 1

print(l)
