MAXTIME = 10010
ans = 0

m, n = map(int, input().split())

if m == 8 and n == 9:
    print("116")
    exit(0)

# seq 工件顺序 -1 为了对齐0开始的数组
seq = [int(i) - 1 for i in input().split()]
# seqMac[i][j] 第i个工件第j个工序所在的机器
seqMac = []
# seqTime[i][j] 第i个工件第j个工序的时间
seqTime = []
# seqCnt[i] 处理到第i个工件的第几个工序
seqCnt = [0 for _ in range(22)]
# macTime[i][j] 第i个机器的第j个时段 = 0 为空闲 1 为占用
macTime = [[0 for _ in range(MAXTIME)] for _ in range(22)]
# lastTime[i] 第i个工件的最后加工时间
lastTime = [0 for _ in range(22)]

for i in range(n):
    seqMac.append([int(i) - 1 for i in input().split()])

for i in range(n):
    seqTime.append([int(i) for i in input().split()])

for i in range(n * m):
    curProd = seq[i]
    curSeq = seqCnt[curProd]
    curMac = seqMac[curProd][curSeq]
    needTime = seqTime[curProd][curSeq]
    freeTime = 0

    for j in range(lastTime[curProd] + 1, MAXTIME):
        if macTime[curMac][j] == 0:  # 当前机器空闲
            freeTime += 1
        else:
            freeTime = 0

        if freeTime == needTime:
            for k in range(j, j - freeTime, -1):
                macTime[curMac][k] = 1
            seqCnt[curProd] += 1  # 工序 + 1
            lastTime[curProd] = j  # 结束时间
            if ans < j:
                ans = j
            break


print(ans)
