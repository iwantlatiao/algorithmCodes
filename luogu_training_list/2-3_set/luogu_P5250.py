import sys
from bisect import bisect_left

MAXN = 200000 + 5
input = sys.stdin.readline
woodDict = {}  # 看了别人代码，其实可以不用字典维护
woodList = []  # 只需要用 list 即可

N = int(input().strip())
for _ in range(N):
    op, l = map(int, input().strip().split())
    if op == 1:  # 进货
        if woodDict.get(l, None) == None:
            woodDict[l] = 1
            index = bisect_left(woodList, l)
            woodList.insert(index, l)
        else:
            print("Already Exist")
    else:  # 出货
        if len(woodList) == 0:
            print("Empty")
        else:
            index = bisect_left(woodList, l)
            if index == 0:
                print(woodList[index])
                woodDict.pop(woodList[index]), woodList.pop(index)
            elif index == len(woodList):
                print(woodList[index - 1])
                woodDict.pop(woodList[index - 1]), woodList.pop(index - 1)
            elif l - woodList[index - 1] <= woodList[index] - l:
                print(woodList[index - 1])
                woodDict.pop(woodList[index - 1]), woodList.pop(index - 1)
            else:
                print(woodList[index])
                woodDict.pop(woodList[index]), woodList.pop(index)
