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
for indX in range(1, len(numMap)):
    for indY in range(0, indX):
        x, y = numMap[indX], numMap[indY]
        xQ, yQ = num[x], num[y]
        if y + y == x:
            if xQ >= 2 and yQ >= 2:
                ans = (ans + ((xQ * (xQ - 1)) >> 1) * ((yQ * (yQ - 1) >> 1))) % MODNUM
        elif y + y < x:
            z = x - y
            zQ = num[z]
            if xQ >= 2 and zQ >= 1:
                ans = (ans + ((xQ * (xQ - 1)) >> 1) * yQ * zQ) % MODNUM
        else:
            break


print(ans)
