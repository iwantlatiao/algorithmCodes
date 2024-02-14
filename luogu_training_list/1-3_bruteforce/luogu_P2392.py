MAXTIME = 300000


def search(curD, curT):
    if curD >= len(time) - 1:
        global singleAns
        curmaxT = max(curT, timeSum - curT)
        singleAns = min(singleAns, curmaxT)
        return
    search(curD + 1, curT)
    search(curD + 1, curT + time[curD + 1])


ans = 0
s1, s2, s3, s4 = map(int, input().split())
for t in range(4):
    time = [int(i) for i in input().split()]
    timeSum = sum(time)
    singleAns = timeSum
    search(0, 0)
    search(0, time[0])
    ans += singleAns

print(ans)
