inputList = input().split()
str, N = inputList[0], int(inputList[1]) - 1
lenStr = len(str)
index, t = N, lenStr

# 字符串什么时候长度超过 N
while t < N:
    t <<= 1

# 讨论在前半段或后半段
while t > lenStr:
    t >>= 1
    if index < t:
        continue
    if index == t:
        index -= 1
    else:
        index -= t + 1

print(str[index])
