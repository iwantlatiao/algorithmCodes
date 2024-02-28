from bisect import bisect_left, bisect_right


N, C = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

ans = 0
for cur in num:
    a = cur + C
    iL, iR = bisect_left(num, a), bisect_right(num, a)
    if iL == len(num):  # 超出数组索引
        continue
    elif iL == iR:  # 没找到
        continue
    else:
        ans += iR - iL

print(ans)
