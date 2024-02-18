MAXPOW = 15
N = int(input())
powNum = [1]
for i in range(14):
    powNum.append(powNum[i] << 1)


def search(x):
    # 不需 while x > 0, 这个循环完成后 x = 0
    for i in range(14, -1, -1):
        if x < powNum[i]:
            continue
        x -= powNum[i]
        if i == 1:
            print("2", end="")
        elif i == 0 or i == 2:
            print("2({})".format(i), end="")
        else:
            print("2(", end="")
            search(i)
            print(")", end="")
        if x > 0:
            print("+", end="")


search(N)
