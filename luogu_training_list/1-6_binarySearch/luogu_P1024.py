def func(x):
    return a * x * x * x + b * x * x + c * x + d


a, b, c, d = map(float, input().split())
ans = []

for x in range(-100, 100):
    if func(x) == 0:
        print("{:.2f}".format(x), end=" ")
    elif func(x) * func(x + 1) < 0:
        l, r = x, x + 1
        while r - l >= 0.0001:
            mid = (l + r) / 2
            if func(l) * func(mid) <= 0:
                r = mid
            else:
                l = mid
        if abs(l) < 0.01:
            l = 0
        print("{:.2f}".format(l), end=" ")
