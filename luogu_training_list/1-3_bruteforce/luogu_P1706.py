from itertools import permutations

n = int(input())
for iter in permutations(range(n)):
    for j in range(n):
        print("{:5}".format(int(iter[j]) + 1), end="")
    print()
