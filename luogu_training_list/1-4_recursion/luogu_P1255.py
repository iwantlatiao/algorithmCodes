N = int(input())
f = [0, 1, 2]
for i in range(3, N + 1):
    f.append(f[i - 1] + f[i - 2])

print(f[N])
