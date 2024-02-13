from math import sqrt
from bisect import bisect_left


# 输入 x 生成一个或多个回文数
def generator(x):
    # 输入 x = 123
    num, tmp, mul = 0, x, 1
    while tmp > 0:
        num = num * 10 + tmp % 10
        tmp //= 10
        mul *= 10

    # 此时 num = 321 tmp = 0 mul = 1000
    # 接下来处理 32123 的情况
    global l
    tmp = (num // 10) * mul + x
    if tmp <= b:
        l.append(tmp)

    # 接下来处理 321123 3210123 ...
    tmp = num * mul + x
    while tmp <= b:
        l.append(tmp)
        mul *= 10
        tmp = num * mul + x


def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


l = []
a, b = map(int, input().split())
for i in range(1, 10000):
    generator(i)

l.sort()
low = bisect_left(l, a)

l = l[low:]
for i in range(len(l)):
    if isPrime(l[i]):
        print(l[i])
