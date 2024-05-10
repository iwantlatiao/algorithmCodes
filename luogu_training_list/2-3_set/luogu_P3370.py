import sys

MAXN, BASE, MOD = 10000, 128, 1061109567
input = sys.stdin.readline
num = []
str = {}
ans = 0


def hash(s):
    res = 0
    for i in range(len(s)):
        res = (res * BASE + ord(s[i])) % MOD
    return res


N = int(input())
for _ in range(N):
    string = input().strip()
    str[string] = 1
    # num.append(hash(string))

# num.sort()
# if N > 0:
#     ans = 1
#     for i in range(1, N):
#         if num[i - 1] != num[i]:
#             ans += 1

print(len(str.keys()))
