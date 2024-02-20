N, T = map(int, input().split())
item = []
for _ in range(N):
    w, v = map(int, input().split())
    item.append([w, v, v / w])

item.sort(key=lambda x: -x[2])

ans = 0
for it in item:
    if T <= 0:
        break
    if T >= it[0]:
        ans += it[1]
        T -= it[0]
    else:
        ans += T * it[2]
        T = 0

print("{:.2f}".format(ans))
