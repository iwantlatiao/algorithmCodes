import itertools


N, R = map(int, input().split())
iter = itertools.combinations(range(N), R)
for it in iter:
    for j in range(R):
        print("{:3d}".format(int(it[j]) + 1), end="")
    print()
