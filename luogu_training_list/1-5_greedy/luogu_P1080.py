n = int(input())
l = []
king = [0, 0]
king[0], king[1] = map(int, input().split())
for i in range(n):
    a, b = map(int, input().split())
    l.append([a, b])

l.sort(key=lambda x: (x[0] * x[1]))
mul = king[0]
ans = mul // l[0][1]

for i in range(1, n):  # from 2 to n
    mul *= l[i - 1][0]
    tmp = mul // l[i][1]
    ans = max(ans, tmp)

print(ans)
