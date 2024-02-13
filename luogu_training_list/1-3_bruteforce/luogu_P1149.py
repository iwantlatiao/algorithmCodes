MAXNUM = 1000
ans = 0
N = int(input())
N -= 4
need = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for i in range(10, (1 + MAXNUM) << 1):
    num, used = i, 0
    while num > 0:
        used += need[num % 10]
        num //= 10
    need.append(used)

for i in range(MAXNUM):
    for j in range(MAXNUM):
        k = i + j
        if need[i] + need[j] + need[k] == N:
            ans += 1
            if k >= 100:
                print(i, j, k)

print(ans)
