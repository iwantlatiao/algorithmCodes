N, X = map(int, input().split())
l = list(map(int, input().split()))
ans = 0

for i in range(N - 1):
    if l[i] > X:
        ans += l[i] - X
        l[i] = X
    if l[i] + l[i + 1] > X:
        ans += l[i] + l[i + 1] - X
        l[i + 1] = X - l[i]

print(ans)
