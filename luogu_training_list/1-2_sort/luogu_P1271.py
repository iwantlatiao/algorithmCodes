n, m = map(int, input().split())
numStr = input().split()
num = [int(i) for i in numStr]
bucket = [0 for _ in range(1010)]

for i in range(m):
    bucket[num[i]] += 1

i = 1
while i <= n:
    if bucket[i] > 0:
        print(i, end=" ")
        bucket[i] -= 1  # 改为一次把桶内的全部输出更快
    else:
        i += 1
