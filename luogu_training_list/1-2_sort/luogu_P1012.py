from functools import cmp_to_key


def cmp(a, b):
    if a + b > b + a:  # a 放前面
        return -1
    elif b + a > a + b:  # b 放前面
        return 1
    else:
        return 0


n = int(input())
numStr = [i for i in input().split()]
ansStr = sorted(numStr, key=cmp_to_key(cmp))
for i in ansStr:
    print(i, end="")
