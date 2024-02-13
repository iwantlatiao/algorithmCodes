# TLE

MAXNUM = 5010
MODNUM = 1000000000 + 7
ans = 0
N = int(input())
num = [0 for _ in range(MAXNUM)]
for i in range(N):
    num[int(input())] += 1

numMap = []
for i in range(MAXNUM):
    if num[i] > 0:
        numMap.append(i)

# y z x x
for i in range(1, len(numMap)):
    j, k = 0, 0
    while j < i:
        y, z, x = numMap[j], numMap[k], numMap[i]
        while y + z < x:
            k += 1
            z = numMap[k]
        xQ, yQ, zQ = num[x], num[y], num[z]
        if y + z == x and xQ >= 2:
            if y == z and zQ >= 2:  # zzxx
                ans += ((xQ * (xQ - 1)) >> 1) * ((yQ * (yQ - 1)) >> 1)
            elif y != z:
                ans += ((xQ * (xQ - 1)) >> 1) * yQ * zQ
        j, k = j + 1, j + 1
        if ans > MODNUM:
            ans %= MODNUM

print(ans)
