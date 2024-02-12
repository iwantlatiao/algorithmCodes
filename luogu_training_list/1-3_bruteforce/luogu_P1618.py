import math


def check(x):
    while x > 0:
        lastDigit = x % 10
        if l[lastDigit] != 0 or lastDigit == 0:
            return False
        else:
            l[lastDigit] = 1  # used
            x //= 10
    return True


def resetL():
    global l
    l = [0 for _ in range(10)]  # 只用 1 ~ 9
    l[0] = 1


A, B, C = map(int, input().split())
if A == 0:
    print("No!!!")
    exit(0)

divide = math.gcd(math.gcd(A, B), C)
A, B, C = A // divide, B // divide, C // divide
l = [0 for _ in range(10)]  # 只用 1 ~ 9
l[0] = 1
k = 0


for i in range(123, 987 + 1, 1):
    if i % A != 0:
        continue
    nowA, nowB, nowC = i, i // A * B, i // A * C
    if check(nowA) and check(nowB) and check(nowC):
        print(nowA, nowB, nowC)
        k += 1
    resetL()

if k == 0:
    print("No!!!")
