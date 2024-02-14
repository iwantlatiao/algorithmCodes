MAXNUM = 20
f = [[1 for _ in range(MAXNUM)]]
for _ in range(MAXNUM - 1):
    f.append([0 for _ in range(MAXNUM)])

N = int(input())
for i in range(1, N + 1):
    f[i][0] = f[i - 1][1]
    for j in range(1, N - i + 1):
        f[i][j] = f[i - 1][j + 1] + f[i][j - 1]
print(f[N][0])
