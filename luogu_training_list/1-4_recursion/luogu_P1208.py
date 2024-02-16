MAXNUM = 1005
f = [0]

N = int(input())
f.append(1)
for i in range(2, N + 1):
    f.append(1)
    for j in range(1, (i >> 1) + 1):
        f[i] += f[j]

print(f[N])
