import sys

MAXN = 200000 + 5
input = sys.stdin.readline
strDict = {}
ans = 0

N = int(input().strip())
for _ in range(N):
    sA, sB = input().split()
    sA = sA[:2]
    if strDict.get(sA + sB, None) == None:
        strDict[sA + sB] = 1
    else:
        strDict[sA + sB] += 1

    res = strDict.get(sB + sA, None)
    if res != None and sA != sB:
        ans += strDict[sB + sA]

print(ans)
