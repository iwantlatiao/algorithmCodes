arr = input()
K = int(input())
num = []
for i in range(len(arr)):
    if "0" <= arr[i] and arr[i] <= "9":
        num.append(int(arr[i]))

num.append(-1)  # -1 和 任何数比都是降序
lenNum = len(num)
frontZero = True

i = 0
while K > 0:
    if num[i] > num[i + 1]:
        num[i : lenNum - 1] = num[i + 1 : lenNum]
        lenNum -= 1
        K -= 1
        if i > 0:
            i -= 1
    else:
        i += 1

i = 0
while num[i] == 0:
    i += 1

if i >= lenNum - 1:
    print(0)
else:
    for j in range(i, lenNum - 1):
        print(num[j], end="")
