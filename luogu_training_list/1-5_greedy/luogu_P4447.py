def setLast():
    global lastNum, lastPopu, sortList, i
    lastNum, lastPopu = sortList[i][0], sortList[i][1]
    sortList[i][1] -= 1

    if sortList[i][1] == 0:
        sortList.pop(i)
        if i >= len(sortList):  # 到末尾了
            resetLen(newLen=0)
    else:
        i += 1


def resetLen(newLen):
    global minLen, curLen, i
    minLen = min(minLen, curLen)
    curLen = newLen
    i = 0


MAXNUM = 100000
N = int(input())
ability = list(map(int, input().split()))

tinymap = {}
for item in ability:
    if tinymap.get(item) == None:
        tinymap[item] = 1
    else:
        tinymap[item] += 1

listKey = list(tinymap.keys())
listVal = list(tinymap.values())
tinyList = [[listKey[i], listVal[i]] for i in range(len(listKey))]
sortList = sorted(tinyList, key=lambda x: x[0])

curLen, minLen = 0, MAXNUM
i, lastNum, lastPopu = 0, 0, 0

while len(sortList) > 0:
    if minLen == 1:
        print("1")
        quit(0)

    if i >= len(sortList):
        resetLen(newLen=0)
    # 队列的第一个
    elif curLen == 0:
        curLen = 1
        setLast()
    # 可以加入队列的条件:
    # 1. 连续 2. 前一个人数 <= 后一个人数
    elif lastNum + 1 == sortList[i][0] and lastPopu <= sortList[i][1]:
        curLen += 1
        setLast()
    else:
        resetLen(newLen=0)


# minLen = min(minLen, curLen)
print(minLen)
